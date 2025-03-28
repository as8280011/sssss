# room.py

class Room:
    """
    Represents a hotel room and its properties such as type, amenities, price, and availability.
    """

    def __init__(self, room_number, room_type, amenities, price_per_night, availability_status=True):
        self._room_number = room_number
        self._room_type = room_type
        self._amenities = amenities  # list of strings
        self._price_per_night = price_per_night
        self._availability_status = availability_status

    # Getters and setters
    def get_room_number(self):
        return self._room_number

    def set_room_number(self, number):
        self._room_number = number

    def get_price(self):
        return self._price_per_night

    def set_price(self, price):
        self._price_per_night = price

    def check_availability(self):
        """Returns whether the room is currently available."""
        return self._availability_status

    def update_room_status(self, status):
        """Updates the room’s availability status."""
        self._availability_status = status

    def get_room_details(self):
        """Returns a string with room information."""
        return f"Room {self._room_number} - Type: {self._room_type}, Price: ${self._price_per_night}/night"


    def calculate_price(self, nights):
        """Calculates price based on number of nights."""
        return self._price_per_night * nights

    def add_amenity(self, amenity):
        """Adds an amenity to the room."""
        if amenity not in self._amenities:
            self._amenities.append(amenity)

    def remove_amenity(self, amenity):
        """Removes an amenity from the room."""
        if amenity in self._amenities:
            self._amenities.remove(amenity)

    def __str__(self):
        return self.get_room_details()
