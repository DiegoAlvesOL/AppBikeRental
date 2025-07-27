"""
This module manages rental-related operations including creation,
cost calculation, and rental period handling.
"""

import json
import os.path

from datetime import datetime, timedelta, date
from tabulate import tabulate
from models.rental import Rental
from services.bike_service import available_bike, register_new_bike, valid_bike_id, set_bike_unavailable, \
    set_bike_available
from services.customer_service import valid_customer_id, register_new_customer
from utils.data_loader import load_rentals, load_rental_cost, load_bikes, load_customers

# Defines the base path to the rentals data JSON file
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_data_rentals = os.path.join(base_dir, "../data/rentals.json")

# Generates a new rental ID based on the last registered rental
def generate_rental_id():
    rentals = load_rentals()
    if not rentals:
        return "0001"
    last_rental = rentals[-1]
    last_id = int(last_rental["rental_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)

# Calculates the end date of a rental based on start date, duration and type
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

# Calculates rental cost based on duration and rental type
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

# Saves a new rental into the rentals data file
def create_rental(rental_obj):
    rental_data = rental_obj.to_dict()
    rentals = load_rentals()
    rentals.append(rental_data)

    with open(file_path_data_rentals, "w") as file:
        json.dump(rentals, file, indent=4)

# Handles the full process of registering a new bike rental
def register_new_rent():
    print("\n --- Registering new Rente ---")

    rental_id = generate_rental_id()

    # Loads customers and prompts registration if none are found
    customers = load_customers()
    if not customers:
        print("\n--- There are no registered customers. ---\n")
        option = input("Would you like to register a new customer now? (y/n) :").strip().lower()
        if option == "y":
            register_new_customer()
            customers = load_customers()
        else:
            print("\nOperation cancelled.\n")
            return

    table_data = [[customer["customer_id"], customer["name"]] for customer in customers]
    print(tabulate(table_data, headers=["ID", "Name"], tablefmt="fancy_grid"))

    # Prompts the user to enter a valid customer ID
    while True:
        customer_id = input("Enter with customer id (e.g 0010): ").strip()
        is_valid_customer_id = valid_customer_id(customer_id)
        if is_valid_customer_id:
            break
        else:
            print("Customer ID not found. Please enter a valid ID.")

    # Loads bikes and prompts registration if none are found
    bikes = load_bikes()
    if not bikes:
        print("--- No Bikes registered. ---")
        option = input("Would you like to register a new customer now? (y/n):").strip().lower()
        if option == "y":
            register_new_bike()
        else:
            print("\nOperation cancelled.\n")
            return

    # Displays available bikes for rental
    available_bikes = available_bike()
    if available_bikes:
        print("\nBikes Available:")
        table_data = [[bike["bike_id"], bike["model"], bike["bike_type"]] for bike in available_bikes]
        print(tabulate(table_data, headers=["ID", "Model", "Type of Bike"], tablefmt="fancy_grid"))
    else:
        print("\n No bikes available at the moment")
        return

    # Prompts the user to enter a valid bike ID
    while True:
        bike_id = input("Enter with bike id (e.g 0014): ")
        is_valid_bike_id = valid_bike_id(bike_id)
        if is_valid_bike_id:
            break

    status = "Ongoing"

    # Prompts the user to choose the rental type (hourly or daily)
    while True:
        rental_type = input("Choose rental type (H/D 'H = hourly' or 'D = daily': ").strip().upper()
        if rental_type in ["H", "D"]:
            break
        else:
            print("\nInvalid option.\n Please enter 'H' or 'D'.")

    # Prompts the user to input the rental duration and validates it
    while True:
        user_input = input("Enter with duration for rente, only whole numbers (e.g 5 days or hours): ").strip()

        if not user_input.isdigit():
            print("\nInvalid format.\n Enter an integer number, without letters, dots or commas: ")
        else:
            duration = int(user_input)
            break

    start_rental_date = date.today().isoformat()
    end_rental_date = end_rental(start_rental_date,duration, rental_type)
    total_cost = calculate_cost(duration, rental_type)

    rental_obj = Rental(rental_id,
                        customer_id,
                        bike_id,
                        status,
                        rental_type,
                        duration,
                        start_rental_date,
                        end_rental_date,
                        total_cost
                        )
    set_bike_unavailable(bike_id)
    create_rental(rental_obj)

    print("\n --- Rental successfully registered. --- \n")


# Returns a list of rentals that are currently ongoing
def get_ongoing_rentals():
    rentals = load_rentals()
    ongoing_rentals = []
    for rental in rentals:
        if rental["status"] == "Ongoing":
            ongoing_rentals.append(rental)
    return ongoing_rentals


# Prompts the user to select a rental from the ongoing list using the rental ID
def select_rental_by_id(ongoing_rentals):
    rental_id = input("Enter the rental ID to complete the rental: ").strip()
    for rental in ongoing_rentals:
        if rental["rental_id"] == rental_id:
            return rental
    return None


# Updates the rental record in the file by changing its status to "Completed"
def update_rental_record(updated_rental):
    rentals = load_rentals()
    for rental in rentals:
        if rental["rental_id"] == updated_rental["rental_id"]:
            rental["status"] = updated_rental["status"]
            break
    with open(file_path_data_rentals, "w") as file:
        json.dump(rentals, file, indent=4)

# Handles the process of returning a bike, including selecting the rental,
# updating its status, and making the bike available again
def register_bike_return():
    print("\n --- Returning a Bike ---\n")

    ongoing_rentals = get_ongoing_rentals()
    if not ongoing_rentals:
        print("There are no ongoing rental at the moment. \n")
        return

    table_data = [[rental["rental_id"], rental["customer_id"],
                   rental["bike_id"], rental["start_rental_date"]]
                  for rental in ongoing_rentals]
    print(tabulate(table_data, headers=["Rental ID", "Customer ID",
                                        "Bike ID", "Start Date"], tablefmt="fancy_grid"))

    rental = select_rental_by_id(ongoing_rentals)
    if not rental:
        print("\nRental ID not found or not ongoing.\n")
        return

    rental["status"] = "Completed"
    update_rental_record(rental)
    set_bike_available(rental)

    print("\n --- Rental successfully completed --- \n")
