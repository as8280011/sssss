from guest import Guest
from room import Room
from booking import Booking
from invoice import Invoice
from service_request import ServiceRequest
from review import Review
from datetime import date

# 1️⃣ Guest Account Creation (2 examples)
print("📌 Test Case 1: Guest Account Creation")
guest1 = Guest("Alice", "111-222", "alice@example.com", "alice01", "pass123", 100, [], "Gold", date.today())
guest2 = Guest("Bob", "333-444", "bob@example.com", "bob99", "bobpass", 50, [], "Silver", date.today())
print(guest1)
print(guest2)

# 2️⃣ Searching for Available Rooms
print("\n📌 Test Case 2: Searching Available Rooms")
room1 = Room("101", "Suite", ["Wi-Fi", "TV"], 200.0, True)
room2 = Room("102", "Double", ["Wi-Fi"], 150.0, False)
available_rooms = [room for room in [room1, room2] if room.check_availability()]
for room in available_rooms:
    print("Available:", room)

# 3️⃣ Making a Room Reservation
print("\n📌 Test Case 3: Making a Room Reservation")
booking1 = Booking("B001", date(2025, 4, 1), date(2025, 4, 3), guest1, room1)
booking2 = Booking("B002", date(2025, 4, 5), date(2025, 4, 7), guest2, room2)
print(booking1)
print(booking2)

# 4️⃣ Booking Confirmation Notification
print("\n📌 Test Case 4: Booking Confirmation Notification")
booking1.send_confirmation_email()
booking2.send_confirmation_email()

# 5️⃣ Invoice Generation
print("\n📌 Test Case 5: Invoice Generation")
invoice1 = Invoice("INV001", room1.calculate_price(2), "Credit Card")
invoice2 = Invoice("INV002", room2.calculate_price(2), "Mobile Wallet")
invoice1.generate_invoice()
invoice2.generate_invoice()
print(invoice1)
print(invoice2)

# 6️⃣ Processing Different Payment Methods
print("\n📌 Test Case 6: Payment Method Updates")
invoice1.set_payment_method("PayPal")
invoice2.set_payment_method("Debit Card")
print(invoice1)
print(invoice2)

# 7️⃣ Displaying Reservation History
print("\n📌 Test Case 7: Displaying Reservation History")
guest1._reservation_history.append(booking1)
guest2._reservation_history.append(booking2)
print(guest1.view_reservation_history())
print(guest2.view_reservation_history())

# 8️⃣ Cancel Booking
print("\n📌 Test Case 8: Booking Cancellation")
booking1.cancel_booking()
booking2.cancel_booking()
print(f"Room {room1.get_room_number()} availability:", room1.check_availability())
print(f"Room {room2.get_room_number()} availability:", room2.check_availability())
