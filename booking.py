# booking.py

from datetime import date

class Booking:
    """
    Represents a hotel room booking made by a guest.
    """

    def __init__(self, booking_id, checkin_date, checkout_date, guest, room):
        self._booking_id = booking_id
        self._checkin_date = checkin_date
        self._checkout_date = checkout_date
        self._guest = guest
        self._room = room
        self._invoice = None         # Composition: will hold an Invoice object
        self._service_requests = []  # Aggregation: list of ServiceRequest objects

    # Getters and setters
    def get_booking_id(self):
        return self._booking_id

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def get_guest(self):
        return self._guest

    def get_room(self):
        return self._room

    def confirm_booking(self):
        """Simulates confirming the booking."""
        print(f"Booking {self._booking_id} confirmed for Guest: {self._guest.get_name()}")

    def cancel_booking(self):
        """Cancels the booking and marks the room as available again."""
        self._room.update_room_status(True)
        print(f"Booking {self._booking_id} cancelled and room {self._room.get_room_number()} is now available.")

    def modify_booking_dates(self, new_checkin, new_checkout):
        """Allows changing the check-in/check-out dates."""
        self._checkin_date = new_checkin
        self._checkout_date = new_checkout
        print(f"Booking {self._booking_id} dates updated.")

    def send_confirmation_email(self):
        """Simulates sending a confirmation message to the guest."""
        print(f"Confirmation sent to {self._guest.get_email()} for booking {self._booking_id}.")

    def add_service_request(self, service_request):
        """Adds a service request to the booking."""
        self._service_requests.append(service_request)

    def set_invoice(self, invoice):
        """Attaches an invoice to the booking (composition)."""
        self._invoice = invoice

    def __str__(self):
        return f"Booking ID: {self._booking_id}, Room: {self._room}, Guest: {self._guest.get_name()}"
