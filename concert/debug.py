from models import Band, Venue, Concert, session

# Example: Get the first band from the database
band = session.query(Band).first()


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
