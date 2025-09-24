from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {
                "title": "Beachside Villa",
                "description": "A relaxing villa by the beach.",
                "price_per_night": 120.00,
                "location": "Malibu",
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin with mountain views.",
                "price_per_night": 90.00,
                "location": "Aspen",
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "price_per_night": 150.00,
                "location": "New York",
            },
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
