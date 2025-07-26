import json
import os.path
from json import JSONDecodeError

"""
This module centralizes all data loading functions from JSON files.
"""

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Load bike data from JSON file.
FILE_PATH_DATA_BIKES = os.path.join(BASE_DIR, "../data/bikes.json")
def load_bikes():
    if os.path.exists(FILE_PATH_DATA_BIKES):
        with open(FILE_PATH_DATA_BIKES, "r") as file:
            try:
                data_bikes = json.load(file)
            except JSONDecodeError:
                data_bikes = []
            return data_bikes
    return []


#Load customer data from JSON file.
FILE_PATH_DATA_CUSTOMERS = os.path.join(BASE_DIR, "../data/customers.json")
def load_customers():

    if os.path.exists(FILE_PATH_DATA_CUSTOMERS):
        with open(FILE_PATH_DATA_CUSTOMERS, "r") as file:
            try:
                data_customers = json.load(file)
            except JSONDecodeError:
                data_customers = []
            return  data_customers
    return []


# Load rental data from JSON file.
FILE_PATH_DATA_RENTALS = os.path.join(BASE_DIR, "../data/rentals.json")
def load_rentals():

    if os.path.exists(FILE_PATH_DATA_RENTALS):
        with open(FILE_PATH_DATA_RENTALS, "r")as file:
            try:
                data_rentals = json.load(file)
            except JSONDecodeError:
                data_rentals = []
            return data_rentals
    return []

# Load rental cost rates from JSON file.
FILE_PATH_DATA_RENTAL_COST = os.path.join(BASE_DIR, "../utils/rental_rates.json")
def load_rental_cost():
    if os.path.exists(FILE_PATH_DATA_RENTAL_COST):
        with open(FILE_PATH_DATA_RENTAL_COST, "r") as file:
            try:
                data_rental = json.load(file)
                if isinstance(data_rental, dict):
                    return data_rental
                else:
                    return {}
            except JSONDecodeError:
                return {}
    return {}

