from operator import truediv

from models.bike import Bike
from models.customer import Customer
from models.rental import Rental
from services.bike_service import add_bike, generate_bike_id, load_bike, set_bike_unavailable
from datetime import date
from services.customer_service import load_customer
from tabulate import tabulate
from services.rental_service import calculate_cost, end_rental, available_bike, create_rental


from services.customer_service import add_customer, generate_customer_id
from services.rental_service import load_customers, generate_rental_id

print("+","="*37,"+")
print("| WELCOME TO THE APP BIKE RENTAL SYSTEM |")
print("+","="*37,"+\n")

while True:
    print("+","="*37, "+")
    print("| 1 - Add new bike", " "*20,"|")
    print("| 2 - Register customer", " "*15,"|")
    print("| 3 - Rent a bike", " "*21,"|")
    print("| 4 - Return a bike", " "*19, "|")
    print("| 5 - Show all bikes"," "*18,"|")
    print("| 6 - Search bike by type or ID", " "*7,"|")
    print("| 0 - Exit and save data", " "*14, "|")
    print("+","="*37, "+\n")

    choice = input("Enter your choice: ").strip()

    if  choice == "0":
        print("+","="*49, "+")
        print("| Thank you for using the App Bike Rental. Goodbye! |")
        print("+","="*49, "+")
        break

    # elif choice == "1": vou fazer essa parte em um segundo momento
    elif choice =="1":
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

    elif choice =="2":
        customer_id = generate_customer_id()
        name = input("Enter with customer name (e.g. Luke Skywalker.): ").strip().title()

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

    elif choice == "3":
        rental_id = generate_rental_id()
        customers = load_customer()

        if not customers:
            print("\n⚠️ Nenhum cliente cadastrado. ⚠️\n")
            option = input("Would you like to register a new customer now? (y/n):").strip().lower()
            if option == "y":
                customer_id = generate_customer_id()
                name = input("Enter with customer name (e.g. Luke Skywalker.): ").strip().title()

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
                customers = load_customer()

            else:
                print("Operation cancelled. Returning to the menu.")


        table_data = [[c["customer_id"], c["name"]] for c in customers]
        print(tabulate(table_data, headers=["ID", "Name"], tablefmt="fancy_grid"))

        valid_customer_ids = []
        for customer in customers:
            valid_customer_ids.append(customer["customer_id"])

        while True:
            customer_id = input("Enter with customer id (e.g 0010): ").strip()
            if customer_id in valid_customer_ids:
                break
            else:
                print("⚠️ Customer ID not found. Please enter a valid ID.")

        available_bikes = available_bike()

        if available_bikes:
            print("\nBikes Available:")
            table_data = [[b["bike_id"], b["model"], b["bike_type"]] for b in available_bikes]
            print(tabulate(table_data, headers=["ID", "Model", "Type of Bike"], tablefmt="fancy_grid"))
        else:
            print("\n No bikes available at the moment")
            table_data = [[b["bike_id"], b["model"], b["bike_type"]] for b in available_bikes]
            print(tabulate(table_data, headers=["ID", "Model", "Type of Bike"], tablefmt="fancy_grid"))

        bikes = load_bike()
        valid_bike_id = []
        for bike in bikes:
            valid_bike_id.append(bike["bike_id"])

        while True:
            bike_id = input("Enter with bike id (e.g 0014): ")
            if bike_id in valid_bike_id:
                break
            else:
                print("⚠️ Bike id not found. Please enter a valid ID.")


        status = "Ongoing"
        while True:
            rental_type = input("Choose rental type (H/D 'H = hourly' or 'D = daily' :").strip().upper()

            if rental_type in ["H", "D"]:
                break
            else:
                print("\n ⚠️Invalid option ⚠️\n. Please enter 'H' or 'D'. ")
        print(rental_type)
        while True:
            user_input = input("Enter with duration for rente, only whole numbers (e.g 5 days or hours): ").strip()

            if not user_input.isdigit():
                print("\n ⚠️Invalid format ⚠️\n. Enter an integer number,\n without letters, dots or commas: ")
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