from sqlalchemy import create_engine, func 
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Creating Bands Table
class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())
    
    # Relationship with concerts
    concerts = relationship('Concert', back_populates='band')
    
    
     # getting all concerts for the band
    def get_concerts(self):
        return self.concerts

    # getting all venues the band has performed at
    def get_venues(self):
        return [concert.venue for concert in self.concerts]
    
    # Playing at a venue on a specific date
    def play_in_venue(self, venue, date):
        new_concert = Concert(date=date, band=self, venue=venue)
        session.add(new_concert)
        session.commit()
        
    # getting all introductions for this band
    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]
    
    # Band with most performances
    @classmethod
    def most_performances(cls):
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

    def __repr__(self):
        return f'Band(id={self.id}, name={self.name}, hometown={self.hometown})'


# Creating Venues Table
class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())
    
    # Relationship with concerts
    concerts = relationship('Concert', back_populates='venue')
    
    # getting all concerts for the venue
    def get_bands(self):
        return [concert.band for concert in self.concerts]
    
    # Playing at a venue on a specific date
    def concert_on(self, date):
        return session.query(Concert).filter_by(venue=self, date=date).first()
    
    # Get the most frequent band at this venue
    def most_frequent_band(self):
        return session.query(Concert.band).filter_by(venue=self).group_by(Concert.band_id).order_by(func.count(Concert.id).desc()).first()

    def __repr__(self):
        return f'Venue(id={self.id}, title={self.title}, city={self.city})'


# Creating Concerts Table
class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String())
    
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    # Relationships
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')
    
    # Checking if concert is a hometown show
    def hometown_show(self):
        return self.band.hometown == self.venue.city
    
    # Introduction for the concert
    def introduction(self):
         return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def __repr__(self):
        return f'Concert(id={self.id}, date={self.date}, band_id={self.band_id}, venue_id={self.venue_id})'
    
    