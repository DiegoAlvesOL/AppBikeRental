import json
import os.path

from utils.data_loader import load_bikes

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path_data_bike = os.path.join(BASE_DIR,"../data/bikes.json")


def generate_bike_id():
    bikes = load_bikes()

    if not bikes:
        return "0001"

    last_bike = bikes[-1]
    last_id = int(last_bike["bike_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)



def add_bike(bike_obj):
    bike_data = bike_obj.to_dict()

    bikes = load_bikes()

    bikes.append(bike_data)

    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)



def set_bike_unavailable(bike_id):
    bikes = load_bikes()

    for bike in bikes:
        if bike ["bike_id"] == bike_id:
            bike ["is_available"] = False
            break
    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)


