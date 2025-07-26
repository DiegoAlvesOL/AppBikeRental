"""
This module handles customer-related operations such as ID generation,
customer registration, validation, and saving customer data.
"""

import json
import os.path
from datetime import date
from models.customer import Customer
from utils.data_loader import load_customers

# Define the base directory and the path to the customers JSON file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path_data_customer = os.path.join(BASE_DIR,"../data/customers.json")

# Generates a new customer ID based on the last customer entry in the file
def generate_customer_id():
    customers = load_customers()

    if not customers:
        return "0001"

    last_customer = customers[-1]
    last_id = int(last_customer["customer_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)

# Adds a new customer to the customer list and saves it to the JSON file
def add_customer(customer_obj):
    customer_data = customer_obj.to_dict()
    customers = load_customers()
    customers.append(customer_data)

    with open(file_path_data_customer, "w") as file:
        json.dump(customers, file, indent= 4)

# Checks if a given customer ID exists in the customers list
def valid_customer_id(input_customer_id):
    customers = load_customers()
    for customer in customers:
        if customer["customer_id"] == input_customer_id:
            return True
    return False

# Registers a new customer by collecting input and saving it to the file
def register_new_customer():
    print("\n --- Registering a new Customer ---")
    customer_id = generate_customer_id()
    name = input("Enter with customer name (e.g. Luke Skywalker.): ").strip().title()

    # Prompts for a valid email address until a correct format is entered
    while True:
        email = input("Enter email: (e.g. luke_skywalker@deathstar.com.): ").strip().lower()
        if "@" in email and "." in email:
            break
        else:
            print("\nInvalid email format. Please try again.\n")

    phone = input("Enter phone number (e.g. 089360-5640): ").replace("-", "").replace(" ","")
    registered_date = date.today().isoformat()

    customer_obj = Customer(customer_id,
                            name,
                            email,
                            phone,
                            registered_date
                            )

    add_customer(customer_obj)
    print("\nCustomer registered successfully!\n")
