from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["id", "title", "description", "price_per_night", "location", "created_at"]


class BookingSerializer(serializers.ModelSerializer):
    listing = serializers.CharField(source="listing.title", read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "listing", "user", "start_date", "end_date", "status", "created_at"]
