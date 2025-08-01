"""
This module provides the main user interface for the App Bike Rental System,
allowing interaction through a command-line menu.
"""
from re import search

from services.bike_service import register_new_bike, display_all_bikes, search_bike
from services.customer_service import register_new_customer
from services.rental_service import register_new_rent, register_bike_return

print("+","="*37,"+")
print("| WELCOME TO THE APP BIKE RENTAL SYSTEM |")
print("+","="*37,"+")

while True:
    print("\n")
    print("+","="*37, "+")
    print("|"," "*15,"HOME", " "*16,"|")
    print("+", "="*37,"+")
    print("| 1 - Add new bike", " "*20,"|")
    print("| 2 - Register customer", " "*15,"|")
    print("| 3 - Rent a bike", " "*21,"|")
    print("| 4 - Return a bike", " "*19, "|")
    print("| 5 - Show all bikes"," "*18,"|")
    print("| 6 - Search bike by type or ID", " "*7,"|")
    print("| 0 - Exit", " "*28, "|")
    print("+","="*37, "+\n")

    choice = input("Enter your choice: ").strip()

    if  choice == "0":
        print("+","="*49, "+")
        print("| Thank you for using the App Bike Rental. Goodbye! |")
        print("+","="*49, "+")
        break



    elif choice =="1":
        register_new_bike()


    elif choice =="2":
        register_new_customer()


    elif choice == "3":
        register_new_rent()


    elif choice == "4":
        register_bike_return()

    elif choice == "5":
        display_all_bikes()

    elif choice =="6":
        search_bike()

