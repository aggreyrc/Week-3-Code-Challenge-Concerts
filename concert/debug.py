from models import Band, Venue, Concert, session

#  Get the first band and venue from the database
band = session.query(Band).first()
venue = session.query(Venue).first()


if band:
    
     # Get all venues the band has performed at
    venues = band.get_venues()
    for venue in venues:
        print(venue)
    
    # Get all concerts played by this band
    concerts_played = band.get_concerts()
    for concert in concerts_played:
        print(concert)
else:
    print("No bands found in the database.")
    

# Band playing in a new venue

if band and venue:
    band.play_in_venue(venue, '2024-09-30')
    print(f"Band {band.name} will perform at {venue.title} on 2024-09-30.")
else:
    print("No bands or venues found in the database.")



# Get the first venue from the database
venue = session.query(Venue).first()

if venue:
    # Get all concerts held at this venue
    concerts = venue.get_concerts()

    print(f"Concerts at {venue.title}:")
    for concert in concerts:
        print(concert)
else:
    print("No venues found in the database.")



# Get all bands that have performed at the venue

venue = session.query(Venue).first()
if venue:
    bands = venue.get_bands()

    print(f"Bands that have performed at {venue.title}:")
    for band in bands:
        print(band)
else:
    print("No venues found in the database.")



# Check if a Concert is a Hometown Show

concert = session.query(Concert).first()

if concert:
    if concert.hometown_show():
        print(f"The concert at {concert.venue.title} is a hometown show for {concert.band.name}.")
    else:
        print(f"The concert at {concert.venue.title} is not a hometown show for {concert.band.name}.")
else:
    print("No concerts found in the database.")
    
  
  
# Get the Introduction for a Concert
    
concert = session.query(Concert).first()

if concert:
    print(f"Introduction for the concert at {concert.venue.title}:")
    print(concert.introduction())
else:
    print("No concerts found in the database.")

