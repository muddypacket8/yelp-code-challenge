class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self._given_name

    def set_given_name(self, given_name):
        self._given_name = given_name

    def family_name(self):
        return self._family_name

    def set_family_name(self, family_name):
        self._family_name = family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def restaurants(self):
        unique_restaurants = set()
        for review in self._reviews:
            unique_restaurants.add(review.restaurant())
        return list(unique_restaurants)

    def add_review(self, restaurant, rating):
        review = review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def all(cls):
        return cls.all_customers

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                matching_customers.append(customer)
        return matching_customers