import json
import os.path
import random
import string

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_data_bike = os.path.join(base_dir,"../data/bikes.json")

def load_bike():
    if os.path.exists(file_path_data_bike):
        with open(file_path_data_bike, "r") as file:
            try:
                data_bike = json.load(file)
            except json.JSONDecodeError:
                data_bike = []
            return data_bike
    return []

def generate_bike_id():
    bikes = load_bike()

    if not bikes:
        return "0001"

    last_bike = bikes[-1]
    last_id = int(last_bike["bike_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)


def add_bike(bike_obj):
    bike_data = bike_obj.to_dict()

    bikes = load_bike()

    bikes.append(bike_data)

    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)

def set_bike_unavailable(bike_id):
    bikes = load_bike()

    for bike in bikes:
        if bike ["bike_id"] == bike_id:
            bike ["is_available"] = False
            break
    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)


