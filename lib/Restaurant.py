class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    def average_star_rating(self):
        total_ratings = sum(review.rating() for review in self._reviews)
        num_reviews = len(self._reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0

    def add_review(self, review):
        self._reviews.append(review)