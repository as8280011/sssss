# guest.py

from user import User
from datetime import date

class Guest(User):
    """
    Represents a hotel guest who inherits from the base User class.
    """

    def __init__(self, name, contact_info, email, user_id, password,
                 loyalty_points, reservation_history, membership_status, account_created_date):
        super().__init__(name, contact_info, email, user_id, password)
        self._loyalty_points = loyalty_points
        self._reservation_history = reservation_history  # list of bookings
        self._membership_status = membership_status
        self._account_created_date = account_created_date

    # Getter and Setter methods
    def get_loyalty_points(self):
        return self._loyalty_points

    def set_loyalty_points(self, points):
        self._loyalty_points = points

    def get_membership_status(self):
        return self._membership_status

    def set_membership_status(self, status):
        self._membership_status = status

    def view_profile(self):
        """Displays guest profile details."""
        return f"{self.get_name()} | Status: {self._membership_status} | Points: {self._loyalty_points}"

    def view_reservation_history(self):
        """Displays all bookings made by the guest."""
        return self._reservation_history

    def earn_loyalty_points(self, points):
        """Adds points to loyalty balance."""
        self._loyalty_points += points

    def redeem_rewards(self):
        """Placeholder for redeeming rewards."""
        print(f"{self.get_name()} redeemed their rewards.")

    def book_room(self, room, checkin_date, checkout_date):
        """Simulates booking a room."""
        print(f"{self.get_name()} booked Room {room} from {checkin_date} to {checkout_date}.")

    def request_service(self, request_type):
        """Simulates sending a service request."""
        print(f"{self.get_name()} requested: {request_type}")

    def leave_review(self, booking, rating, comment):
        """Simulates leaving a review for a booking."""
        print(f"Review by {self.get_name()} for {booking}: {rating}/5 - {comment}")

    def __str__(self):
        return f"Guest({self.get_name()}, Points: {self._loyalty_points})"
