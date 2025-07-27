"""
This module handles operations related to bike management, such as registration,
availability checking, ID generation, and updating bike status.
"""

import json
import os.path
from datetime import date
from models.bike import Bike
from utils.data_loader import load_bikes
from tabulate import tabulate

# Sets the path to the JSON file where bike data is stored
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path_data_bike = os.path.join(BASE_DIR,"../data/bikes.json")

# Generates a new bike ID based on the last bike's ID in the data
def generate_bike_id():
    bikes = load_bikes()
    if not bikes:
        return "0001"
    last_bike = bikes[-1]
    last_id = int(last_bike["bike_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)

# Adds a new bike to the bike list and saves it to the JSON file
def add_bike(bike_obj):
    bike_data = bike_obj.to_dict()
    bikes = load_bikes()
    bikes.append(bike_data)

    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)

# Sets a bike's availability to False (unavailable) by its ID
def set_bike_unavailable(bike_id):
    bikes = load_bikes()

    for bike in bikes:
        if bike["bike_id"] == bike_id:
            bike["is_available"] = False
            break
    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)

# Sets a bike as available by ID
def set_bike_available(bike_id):
    bikes =load_bikes()

    for bike in bikes:
        if bike["bike_id"] == bike_id["bike_id"]:
            bike["is_available"] = True
            break
    with open(file_path_data_bike, "w") as file:
        json.dump(bikes, file, indent=4)


# Validates whether the input bike ID exists and is available for rent
def valid_bike_id(input_bike_id):
    bikes = load_bikes()
    for bike in bikes:
        if bike["bike_id"] == input_bike_id:
            if bike.get("is_available") == True:
                return True
            else:
                print("This bike is currently rented. Please choose notaher one.")
                return False
    print("--- Bike ID not found ---")
    return False

# Returns a list of all bikes that are currently available
def available_bike():
    bikes = load_bikes()
    available = []
    for bike in bikes:
        if bike.get("is_available") == True:
            available.append(bike)
    return available


# function to view all bikes
def display_all_bikes():
    bikes = load_bikes()
    if not bikes:
        print("\n--- No Bikes found. ---")
        return

    table_data = [[bike["bike_id"], bike["model"], bike["bike_type"], bike["is_available"], bike["registered_date"]]
                  for bike in bikes]
    print(tabulate(table_data, headers=["Bike ID", "Model", "Type", "Availabel", "Registration date"], tablefmt="fancy_grid"))


# This function searches for bikes using by bike ID.
def search_bike():
    bikes = load_bikes()
    if not bikes:
        print("--- No bikes available. ---")
        return

    bike_id = input("Enter the bike ID: ").strip()
    for bike in bikes:
        if bike["bike_id"] == bike_id:
            table_data = [[bike["bike_id"], bike["model"], bike["bike_type"], bike["is_available"], bike["registered_date"]]]
            print(tabulate(table_data,headers=["Bike ID", "Model", "Type", "Availabel", "Registration date"], tablefmt="fancy_grid"))


    print("\n--- Bike id not found. ---")


# Handles user input to register a new bike and saves it to the data file
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
    print("\n--- Bike registered successfully! ---\n")