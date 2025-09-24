# ALX Travel App 0x00

This project defines **database models**, **serializers**, and a **data seeder** for a travel booking application.

## Features

- **Models**:
  - `Listing`: Travel listings (title, description, price, location).
  - `Booking`: Bookings with start & end dates, status.
  - `Review`: User reviews with ratings and comments.

- **Serializers**:
  - `ListingSerializer`
  - `BookingSerializer`

- **Seeder**:
  - Adds sample listings (`Beachside Villa`, `Mountain Cabin`, `City Apartment`).

## Commands

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed the database
python manage.py seed
