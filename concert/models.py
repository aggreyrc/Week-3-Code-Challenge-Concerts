from sqlalchemy import create_engine, func 
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///concerts.db')


Base = declarative_base()

# Creating Bands Table
class Band(Base):
    __tablename__ = 'bands'
    
  
    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())
    
    def __repr__(self):
        return f'Band(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'hometown={self.hometown})'
            

# Creating Venues Table
class Venues(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())
    
    def __repr__(self):
        return f'Venue(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'city={self.city})'
    
    

# Creating Concerts Table
class Concerts(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True)
    date = Column(String())
    
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venues', back_populates='concerts')
    
    def __repr__(self):
        return f'Concert(id={self.id}, ' + \
            f'date={self.date}, ' + \
            f'band_id={self.band_id}, ' + \
            f'venue_id={self.venue_id})'
    
    