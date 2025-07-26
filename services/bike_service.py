import json
import os.path
from datetime import date
from models.bike import Bike
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

def register_new_bike():
    print("\n --- Registering a new Bike ---")
    bike_id = generate_bike_id()
    model = input("Enter the bike model (e.g. Trek FX or Caloi 29): ").strip().title()
    bike_type = input("Enter the bike type (e.g. Urban, Montain or Eletric): ").strip().title()
    is_available = True
    registered_date = date.today().isoformat()

    bike_obj = Bike(bike_id,
                    model,
                    bike_type,
                    is_available,
                    registered_date
                    )

    add_bike(bike_obj)
    print("\nBike registered successfully!\n")



def set_bike_unavailable(bike_id):
    bikes = load_bikes()

    for bike in bikes:
        if bike ["bike_id"] == bike_id:
            bike ["is_available"] = False
            break
    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)


