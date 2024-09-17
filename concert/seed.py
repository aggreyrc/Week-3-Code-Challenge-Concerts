from faker import Faker
from models import Band, Venue, Concert, session

faker = Faker()

# Add sample data
for _ in range(10):
    band = Band(name=faker.company(), hometown=faker.city())
    venue = Venue(title=faker.company(), city=faker.city())
    session.add(band)
    session.add(venue)

    # Create concerts for the band at the venue
    for _ in range(3):
        concert = Concert(date=faker.date(), band=band, venue=venue)
        session.add(concert)

session.commit()
