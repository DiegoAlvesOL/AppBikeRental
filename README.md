
# AppBikeRental

This is a Python application that simulates a simple **bike rental system**.  
It was created as part of the *Programming Essentials 2* module for the BSc in Computing & Multimedia program.

## Features implemented

- Register new bikes with ID, model, type, availability, and registration date.
- All bike data is saved into a `.json` file.
- Uses Object-Oriented Programming (OOP) with custom classes.

## Project structure

```
AppBikeRental/
├── main.py
├── models/
│   └── bike.py
├── services/
│   └── bike_service.py
├── data/
│   └── bikes.json
```

##  How to run

Make sure you have Python 3 installed.

1. Clone the repository:
```
git clone https://github.com/yourusername/AppBikeRental.git
```

2. Open the project folder and run the application:
```
python main.py
```

3. Use the menu to register a new bike or access other features.

##  Requirements

- Python 3
- No external libraries needed for this stage.

##  Next steps

- Show all bikes
- Register customers
- Rent and return bikes
- Search by ID or type
