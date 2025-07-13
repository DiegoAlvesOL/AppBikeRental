class Bike:
    def __init__(self, bike_id,
                 model,
                 bike_type,
                 is_available,
                 registered_date):
        self.bike_id = bike_id
        self.model = model
        self.bike_type = bike_type
        self.is_available = is_available
        self.registered_date = registered_date


    def to_dict(self):
        return {
            "bike_id": self.bike_id,
            "model": self.model,
            "bike_type": self.bike_type,
            "is_available": self.is_available,
            "registered_date": self.registered_date
        }