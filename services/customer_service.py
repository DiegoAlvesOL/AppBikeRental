import json
import os.path

from utils.data_loader import load_customers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path_data_customer = os.path.join(BASE_DIR,"../data/customers.json")


def generate_customer_id():
    customers = load_customers()

    if not customers:
        return "0001"

    last_customer = customers[-1]
    last_id = int(last_customer["customer_id"])
    next_id = last_id + 1
    return "{:04d}".format(next_id)


def add_customer(customer_obj):
    customer_data = customer_obj.to_dict()

    customers = load_customers()
    customers.append(customer_data)

    with open(file_path_data_customer, "w") as file:
        json.dump(customers, file, indent= 4)
