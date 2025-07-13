from models.bike import Bike
from services.bike_service import add_bike, generate_bike_id
from datetime import date

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
        model = input("Enter the bike model: ").strip().title()
        bike_type = input("Enter the bike type: ").strip().title()
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
