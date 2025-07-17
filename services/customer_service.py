import json
import os.path
import random
import string
from json import JSONDecodeError

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path_data_customer = os.path.join(base_dir,"../data/customers.json")

def load_customer():
    if os.path.exists(file_path_data_customer):
        with open(file_path_data_customer, "r") as file:
            try:
                data_customer = json.load(file)
            except JSONDecodeError:
                data_customer = []
            return data_customer
    return []


def generate_customer_id():
    customers = load_customer()

    if not customers:
        return "0001"

    last_customer = customers[-1]

    last_id = int(last_customer["customer_id"])

    next_id = last_id + 1

    return "{:04d}".format(next_id)

    # letter_digits_id = string.digits + string.ascii_lowercase
    #
    # id_for_customer = ""
    #
    # for i in range(10):
    #     id_for_customer = id_for_customer + random.choice(letter_digits_id)
    # return id_for_customer


def add_customer(customer_obj):
    customer_data = customer_obj.to_dict()

    customers = load_customer()

    customers.append(customer_data)

    with open(file_path_data_customer, "w") as file:
        json.dump(customers, file, indent= 4)
