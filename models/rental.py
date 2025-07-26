class Rental:
    def __init__(self, rental_id,
                 customer_id,
                 bike_id,
                 status,
                 rental_type,
                 duration,
                 start_rental_date,
                 end_rental_date,
                 total_cost):

        self.rental_id = rental_id
        self.customer_id = customer_id
        self.bike_id = bike_id
        self.status = status
        self.rental_type = rental_type
        self.duration = duration
        self.start_rental_date = start_rental_date
        self.end_rental_date = end_rental_date
        self.total_cost = total_cost

    def to_dict(self):
        return {
            "rental_id": self.rental_id,
            "customer_id": self.customer_id,
            "bike_id": self.bike_id,
            "status": self.status,
            "rental_type": self.rental_type,
            "duration": self.duration,
            "start_rental_date": self.start_rental_date,
            "end_rental_date": self.end_rental_date,
            "total_cost": self.total_cost
        }
