import json
import os.path

from datetime import datetime, timedelta
from utils.data_loader import load_rentals, load_rental_cost, load_bikes

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_data_rentals = os.path.join(base_dir, "../data/rentals.json")


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


