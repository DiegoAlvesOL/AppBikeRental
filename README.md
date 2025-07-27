
# AppBikeRental

**AppBikeRental** is an academic project developed for the *Programming Essentials 2* module at **Dorset College**.  
The goal of this software is to provide a console-based system for managing **bike rentals**, using **Object-Oriented Programming (OOP)** principles and persistent storage in JSON format.

## Features

This application offers the following functionalities via a simple text-based menu:

1. **Show all bikes**
2. **Add new bike**
3. **Register customer**
4. **Rent a bike**
5. **Return a bike**
6. **Search bike by type or ID**
0. **Exit and save data**

Each entity (bikes, rentals, and customers) is stored in JSON files for persistence between executions.

## Project Structure

```
bike_rental/
├── data/
│   ├── bikes.json
│   ├── customers.json
│   └── rentals.json
├── models/
│   ├── bike.py
│   ├── customer.py
│   └── rental.py
├── services/
│   ├── bike_service.py
│   ├── customer_service.py
│   └── rental_service.py
├── utils/
│   ├── data_loader.py
├── main.py
```

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/DiegoAlvesOL/AppBikeRental.git
   ```
3. Navigate to the project folder:
   ```bash
   cd AppBikeRental
   ```
4. Run the main application:
   ```bash
   python main.py
   ```

## Requirements

- Python 3
- `tabulate` library (used for table formatting).  
  Install it using:
  ```bash
  pip install tabulate
  ```

## Notes

- All application data is stored locally in JSON format inside the `data/` directory.
- Designed using Object-Oriented Programming and a modular architecture to facilitate future updates or feature expansions.

## Academic Context

This application was developed as part of the *Programming Essentials 2* coursework at **Dorset College**, with the objective of reinforcing software development concepts, file handling, and data persistence using Python.
