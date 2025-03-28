# invoice.py

class Invoice:
    """
    Represents an invoice for a hotel booking.
    """

    def __init__(self, invoice_id, total_amount, payment_method, discounts_applied=None):
        self._invoice_id = invoice_id
        self._total_amount = total_amount
        self._payment_method = payment_method
        self._discounts_applied = discounts_applied

    # Getters and setters
    def get_invoice_id(self):
        return self._invoice_id

    def get_total_amount(self):
        return self._total_amount

    def set_total_amount(self, amount):
        self._total_amount = amount

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, method):
        self._payment_method = method

    def get_discounts_applied(self):
        return self._discounts_applied

    def set_discounts_applied(self, discount_code):
        self._discounts_applied = discount_code

    def generate_invoice(self):
        """Simulates invoice generation."""
        print(f"Invoice {self._invoice_id} generated for ${self._total_amount}.")

    def apply_discount(self, discount_code):
        """Applies a discount code (just simulating here)."""
        self._discounts_applied = discount_code
        print(f"Discount {discount_code} applied.")

    def calculate_total(self):
        """Returns the final amount (after applying any logic if needed)."""
        return self._total_amount

    def __str__(self):
        return f"Invoice(ID: {self._invoice_id}, Total: ${self._total_amount}, Method: {self._payment_method})"
