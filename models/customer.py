class Customer:
    def __init__(self, customer_id,
                 name,
                 email,
                 phone,
                 registered_date):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.registered_date = registered_date

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "registered_date": self.registered_date
        }

