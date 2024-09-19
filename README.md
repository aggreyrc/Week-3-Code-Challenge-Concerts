# Phase 3 Code Challenge: Concerts

# Introduction

This is a project for a simple Concerts management system built using SQLAlchemy and SQLite. This system allows you to manage Bands,venues and concerts themselves and has methods to query the database.

# Project Features

1. Manage Bands: Create bands, list their concerts, and track venues they performed at.
2. Manage Venues: Create venues, list concerts held at each venue, and track bands that have performed there.
3. Manage Concerts: Add concerts with a date, band, and venue.
4. Custom methods for data querying:
        1. Get all concerts for a band.
        2. Get all venues a band has performed at.
        3. Find the most frequent band for a venue.
        4. Check if a concert is a "hometown show."

# Prerequisites

Before you begin, ensure you have the following installed on your local machine:

    -Python 3.x
    -Virtual Environment (optional but recommended)
    -SQLAlchemy library
You can install SQLAlchemy via pip:

    pip install SQLAlchemy

# Setup Instructions

1. Clone the Repository
To clone this project, run the following command in your terminal:

    ```git clone https://github.com/aggreyrc/Week-3-Code-Challenge-Concerts```

2. Navigate to the project directory in the terminal

        cd concert

3. Install Dependencies
Install the required Python packages using:
     
     ```pip install -r requirements.txt```

5. Set Up the Database
Run the seed script to populate the database with some sample data using Faker:

        python seed.py

6. Interact with the Database
You can now run scripts like debug.py to interact with the database, or write your own scripts to explore the functionality.

        python debug.py


