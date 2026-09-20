[README.md](https://github.com/user-attachments/files/32427963/README.md)# DVLA Valid Licence Checker

A Python-based text program designed to check UK vehicle licence plates using DVLA region codes and registration formats.

## Overview

The DVLA Valid Licence Checker provides a simple menu-driven interface with five options:

1. Check whether a licence plate is valid
2. Find the age of a car
3. Find the registration city
4. Generate an example licence plate
5. Quit the program

The program uses a list of DVLA regions and their corresponding licence plate codes to validate user input. It also separates each major task into its own function, making the program easier to organise and use.

## Features

### Licence Plate Validation
Checks whether a licence plate:
- Has 7 characters
- Contains a valid two-letter DVLA region code
- Has two digits in the correct position
- Has three letters in the final position

### Car Age Calculator
Uses the two-digit registration identifier to calculate the vehicle's registration year and estimated age.

### Registration City
Uses the first two characters of the licence plate to identify the corresponding registration area.

### Example Licence Generator
Randomly selects an example from a list of valid licence plates.

### Input Validation
The program repeatedly asks for new input when an invalid menu option or licence plate is entered.

## Technologies Used

- **Python 3**
- `random` module for generating example licence plates
- `datetime` module for date-related functionality
- Lists, loops, functions, conditional statements and input validation

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the Python file in your IDE or terminal.
4. Run the program:

```bash
python main.py
```

## How to Use

When the program starts, a menu is displayed.

Enter a number from **1 to 5**:

```text
1. Check if a Licence Plate is valid
2. Find the age of a car
3. Find the registration city
4. Generate an example Licence Plate
5. Quit
```

Follow the prompts for the selected option. The program will continue asking for input when an invalid value is entered.

## Project Structure

The main program contains separate functions for each menu feature:

- `User_Menu()` – displays and processes the main menu
- `User_Check_License()` – validates a licence plate
- `User_Car_Age()` – calculates vehicle age
- `User_Registration_City()` – identifies the registration city
- `User_Generate_License()` – generates an example licence plate
- `User_Exit()` – handles program exit

## Purpose

This project demonstrates the use of fundamental Python programming concepts, including:

- Variables
- Lists and arrays
- Functions
- `for` and `while` loops
- `if`, `elif` and `else`
- Boolean conditions
- String methods
- Input validation
- Random selection

## Author

**Daniel Oniyide**
