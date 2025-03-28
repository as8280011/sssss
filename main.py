# main.py

from guest import Guest
from room import Room
from booking import Booking
from invoice import Invoice
from service_request import ServiceRequest
from review import Review
from datetime import date

# Step 1: Create a guest
guest1 = Guest(
    name="Alice",
    contact_info="123-456-7890",
    email="alice@example.com",
    user_id="alice01",
    password="securepass",
    loyalty_points=100,
    reservation_history=[],
    membership_status="Gold",
    account_created_date=date(2024, 5, 10)
)

# Step 2: Create a room
room1 = Room(
    room_number="101",
    room_type="Suite",
    amenities=["Wi-Fi", "TV", "Mini-bar"],
    price_per_night=200.0
)

# Step 3: Make a booking
booking1 = Booking(
    booking_id="B001",
    checkin_date=date(2025, 4, 1),
    checkout_date=date(2025, 4, 5),
    guest=guest1,
    room=room1
)

guest1.book_room(room1.get_room_number(), date(2025, 4, 1), date(2025, 4, 5))
booking1.confirm_booking()
booking1.send_confirmation_email()

# Step 4: Generate an invoice
invoice1 = Invoice(
    invoice_id="INV001",
    total_amount=room1.calculate_price(4),
    payment_method="Credit Card"
)
invoice1.generate_invoice()
booking1.set_invoice(invoice1)

# Step 5: Add a service request
service = ServiceRequest(
    request_id="SR001",
    request_type="Room Cleaning"
)
service.submit_request()
booking1.add_service_request(service)

# Step 6: Leave a review
review = Review(
    review_id="RV001",
    rating=5,
    comments="Amazing stay, very clean and comfortable!"
)
review.submit_review()
guest1.leave_review(booking1.get_booking_id(), review.get_rating(), review.get_comments())

# Print summary
print("\n--- SUMMARY ---")
print(guest1)
print(room1)
print(booking1)
print(invoice1)
print(service)
print(review)