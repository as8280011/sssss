# user.py

class User:
    """
    Base class for all users in the Royal Stay Hotel system.
    """

    def __init__(self, name, contact_info, email, user_id, password):
        # Protected attributes
        self._name = name
        self._contact_info = contact_info
        self._email = email
        self._user_id = user_id
        self.__password = password  # Private

    # Getter and Setter methods
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_contact_info(self):
        return self._contact_info

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def login(self):
        """Simulates user login."""
        print(f"{self._name} has logged in.")

    def logout(self):
        """Simulates user logout."""
        print(f"{self._name} has logged out.")

    def update_profile(self):
        """Placeholder for updating profile."""
        print("Profile updated.")

    def view_account_details(self):
        """Returns account details."""
        return f"Name: {self._name}, Email: {self._email}, Contact: {self._contact_info}"

    def reset_password(self, new_password):
        """Allows resetting the password."""
        self.__password = new_password
        print("Password has been reset.")

    def delete_account(self):
        """Simulates account deletion."""
        print(f"Account for {self._name} has been deleted.")

    def __str__(self):
        return f"User(Name: {self._name}, Email: {self._email})"
