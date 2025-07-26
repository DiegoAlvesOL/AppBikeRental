import json
import os.path
from json import JSONDecodeError
from datetime import datetime, timedelta

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_data_bikes = os.path.join(base_dir,"../data/bikes.json")
file_path_data_customers = os.path.join(base_dir,"../data/customers.json")
file_path_data_rentals = os.path.join(base_dir, "../data/rentals.json")
file_path_data_rental_cost = os.path.join(base_dir, "../utils/rental_rates.json")


def load_bikes():
    if os.path.exists(file_path_data_bikes):
        with open(file_path_data_bikes, "r") as file:
            try:
                data_bikes = json.load(file)
            except JSONDecodeError:
                data_bikes = []
            return data_bikes
    return []


def load_customers():
    if os.path.exists(file_path_data_customers):
        with open(file_path_data_customers, "r") as file:
            try:
                data_customers = json.load(file)
            except JSONDecodeError:
                data_customers = []
            return  data_customers
    return []


def load_rentals():
    if os.path.exists(file_path_data_rentals):
        with open(file_path_data_rentals, "r")as file:
            try:
                data_rentals = json.load(file)
            except JSONDecodeError:
                data_rentals = []
            return data_rentals
    return []


def load_rental_cost():
    if os.path.exists(file_path_data_rental_cost):
        with open(file_path_data_rental_cost, "r") as file:
            try:
                data_rental = json.load(file)
                if isinstance(data_rental, dict):
                    return data_rental
                else:
                    return {}
            except JSONDecodeError:
                return {}
    return {}


def generate_rental_id():
    rentals = load_rentals()

    if not rentals:
        return "0001"

    last_rental = rentals[-1]

    last_id = int(last_rental["rental_id"])
    next_id = last_id + 1

    return "{:04d}".format(next_id)


def end_rental(start_rental_date,duration, rental_type):
    start_dt = datetime.fromisoformat(start_rental_date)
    if rental_type == "H":
        duration_hours = duration
        duration_hours = timedelta(hours=duration_hours)
        end_dt = start_dt + duration_hours
    elif rental_type == "D":
        duration_days = duration
        duration_days = timedelta(days=duration_days)
        end_dt = start_dt + duration_days
    else:
        print("Invalid rental type")
        return start_dt
    return end_dt.date().isoformat()


def calculate_cost(duration, rental_type):
    rates = load_rental_cost()
    if rental_type == "H":
        rate = rates.get("hours", 0)
        end_cost = rate * duration
    elif rental_type == "D":
        rate = rates.get("daily", 0)
        end_cost = rate * duration
    else:
        print("Invalid rental type")
        return 0.0
    return end_cost


def available_bike():
    bikes = load_bikes()

    available = []

    for bike in bikes:
        if bike.get("is_available") == True:
            available.append(bike)

    return available


def create_rental(rental_obj):
    rental_data = rental_obj.to_dict()
    rentals = load_rentals()
    rentals.append(rental_data)

    with open(file_path_data_rentals, "w") as file:
        json.dump(rentals, file, indent=4)


