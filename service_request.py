# service_request.py

class ServiceRequest:
    """
    Represents a service request made by a guest during their stay.
    """

    def __init__(self, request_id, request_type, request_status="Pending"):
        self._request_id = request_id
        self._request_type = request_type
        self._request_status = request_status

    # Getter and Setter methods
    def get_request_id(self):
        return self._request_id

    def get_request_type(self):
        return self._request_type

    def set_request_type(self, request_type):
        self._request_type = request_type

    def get_request_status(self):
        return self._request_status

    def update_request_status(self, new_status):
        self._request_status = new_status
        print(f"Service Request {self._request_id} updated to {new_status}.")

    def submit_request(self):
        """Simulates submitting the request."""
        print(f"Request {self._request_id} for {self._request_type} has been submitted.")

    def cancel_request(self):
        """Cancels the service request."""
        self._request_status = "Cancelled"
        print(f"Request {self._request_id} has been cancelled.")

    def __str__(self):
        return f"Request(ID: {self._request_id}, Type: {self._request_type}, Status: {self._request_status})"
