from models.bike import Bike
from models.customer import Customer
from services.bike_service import add_bike, generate_bike_id
from datetime import date

from services.customer_service import add_customer, generate_customer_id

print("+","="*37,"+")
print("| WELCOME TO THE APP BIKE RENTAL SYSTEM |")
print("+","="*37,"+\n")

while True:
    print("+","="*37, "+")
    print("| 1 - Show all bikes"," "*18,"|")
    print("| 2 - Add new bike", " "*20,"|")
    print("| 3 - Register customer", " "*15,"|")
    print("| 4 - Rent a bike", " "*21,"|")
    print("| 5 - Return a bike", " "*19, "|")
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
    elif choice =="2":
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

    elif choice =="3":
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


