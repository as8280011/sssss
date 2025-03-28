# review.py

class Review:
    """
    Represents a guest's review for their stay.
    """

    def __init__(self, review_id, rating, comments):
        self._review_id = review_id
        self._rating = rating
        self._comments = comments

    # Getter and Setter methods
    def get_review_id(self):
        return self._review_id

    def get_rating(self):
        return self._rating

    def set_rating(self, rating):
        self._rating = rating

    def get_comments(self):
        return self._comments

    def set_comments(self, comments):
        self._comments = comments

    def submit_review(self):
        """Simulates submitting the review."""
        print(f"Review {self._review_id} submitted with {self._rating} stars.")

    def edit_review(self, new_rating, new_comments):
        """Edits an existing review."""
        self._rating = new_rating
        self._comments = new_comments
        print(f"Review {self._review_id} updated.")

    def is_positive(self):
        """Returns True if the rating is 4 or higher."""
        return self._rating >= 4

    def __str__(self):
        return f"Review(ID: {self._review_id}, Rating: {self._rating}/5, Comments: {self._comments})"
