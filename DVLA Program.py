import random
from datetime import datetime


# This program is designed to check the validity of a UK License plate based on the DVLA (Driver and Vehicle Licensing Agency) regions and formats. 
# It provides a user menu with options to check if a License plate is valid, find the age of a car, find the registration city, generate an example License plate, or quit the program.
# The program uses a list of DVLA regions and their corresponding codes to validate the License plate entered by the user. 
# It also includes functions for each menu option, allowing users to interact with the program and receive relevant information based on their input.

DVLA_Regions = [
    ["A", ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"], "Peterborough"],
    ["A", ["AO", "AP", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY"], "Norwich"],
    ["A", ["AV", "AW", "AX", "AY"], "Ipswich"],

    ["B", ["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"], "Birmingham"],

    ["C", ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO"], "Cardiff"],
    ["C", ["CP", "CQ", "CR", "CS", "CT", "CU", "CV"], "Swansea"],
    ["C", ["CW", "CX", "CY"], "Bangor"],

    ["D", ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DI", "DJ", "DK"], "Chester"],
    ["D", ["DL", "DM", "DN", "DO", "DP", "DQ", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY"], "Shrewsbury"],

    ["E", ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EI", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "EQ", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY"], "Chelmsford"],

    ["F", ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FI", "FJ", "FK", "FL", "FM", "FN", "FO", "FP"], "Nottingham"],
    ["F", ["FR", "FS", "FT", "FU", "FV", "FW", "FX", "FY"], "Lincoln"],

    ["G", ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GI", "GJ", "GK", "GL", "GM", "GN", "GO"], "Maidstone"],
    ["G", ["GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY"], "Brighton"],

    ["H", ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ"], "Bournemouth"],
    ["H", ["HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HY"], "Portsmouth"],
    ["H", ["HW"], "Isle of Wight"],

    ["K", ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL"], "Luton"],
    ["K", ["KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY"], "Northampton"],

    ["L", ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LI", "LJ"], "Wimbledon"],
    ["L", ["LK", "LL", "LM", "LN", "LO", "LP", "LQ", "LR", "LS", "LT"], "Stanmore"],
    ["L", ["LU", "LV", "LW", "LX", "LY"], "Sidcup"],

    ["M", ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MI", "MJ", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY"], "Manchester"],

    ["N", ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NI", "NJ", "NK", "NL", "NM", "NN", "NO"], "Newcastle"],
    ["N", ["NP", "NQ", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY"], "Stockton"],

    ["O", ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OI", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OQ", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY"], "Oxford"],

    ["P", ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PI", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PQ", "PR", "PS", "PT"], "Preston"],
    ["P", ["PU", "PV", "PW", "PX", "PY"], "Carlisle"],

    ["R", ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RI", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RQ", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY"], "Reading"],

    ["S", ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ"], "Glasgow"],
    ["S", ["SK", "SL", "SM", "SN", "SO"], "Edinburgh"],
    ["S", ["SP", "SQ", "SR", "SS", "ST"], "Dundee"],
    ["S", ["SU", "SV", "SW"], "Aberdeen"],
    ["S", ["SX", "SY"], "Inverness"],

    ["V", ["VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VI", "VJ", "VK", "VL", "VM", "VN", "VO", "VP", "VQ", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY"], "Worcester"],

    ["W", ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WI", "WJ"], "Exeter"],
    ["W", ["WK", "WL"], "Truro"],
    ["W", ["WM", "WN", "WO", "WP", "WQ", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY"], "Bristol"],

    ["Y", ["YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YI", "YJ", "YK"], "Leeds"],
    ["Y", ["YL", "YM", "YN", "YO", "YP", "YQ", "YR", "YS", "YT", "YU"], "Sheffield"],
    ["Y", ["YV", "YW", "YX", "YY"], "Beverley"],
]

def User_Menu():

    # Displays the main menu to the user and shows all available functions.
    
    print("""         
        ==============================
        DVLA Valid License Checker 
        ==============================

        1. Check if a Licence Plate is valid
        2. Find the age of a car
        3. Find the registration city
        4. Generate an example Licence Plate
        5. Quit

        ==============================
         """)

    # Prompting the user to enter a number between 1-5 for the service required and validating the input
        
    User_Input_License = input("Enter a number between 1-5 for the service required: ")
    while not User_Input_License.isdigit() or int(User_Input_License) > 5 or int(User_Input_License) < 1:
        print("You've entered a number that isn't accepted, please try again.")
        User_Input_License = input("Enter a number between 1-5 for the service required: ")
    # Uses the number inputted to assign the user to a set function within the program
        
    if User_Input_License == "1":
        User_Check_License()
    elif User_Input_License == "2":
        User_Car_Age()
    elif User_Input_License == "3":
        User_Registration_City()
    elif User_Input_License == "4":
        User_Generate_License()
    elif User_Input_License == "5":
        User_Exit()

# 1
def User_Check_License():
        
    while True:
    
        User_License_Plate = input("Please enter the Licence Plate you would like to check, ensure there are no spaces: ") # Prompts the user to enter the Licence Plate they would like to check
        User_License_Plate = User_License_Plate.strip().upper()  # Converts the input to uppercase for consistency 
        
        User_Region_Code = (User_License_Plate[0:2]) # Extracting the first two characters of the license Plate to get the region code, in order to figure out whether the first 2 characters belongs to a valid Licence

        Found_Valid_Region = False

        for region in DVLA_Regions: # Looping through the list of DVLA regions to check if the region code is valid
                if User_Region_Code in region[1]: 
                    Found_Valid_Region = True
                    break

        Requirements = [ # Array that stores the requirements for a valid Licence Plate 
            
            Found_Valid_Region,
            len(User_License_Plate) == 7,
            User_License_Plate[0:2].isalpha(),
            User_License_Plate[2:4].isdigit(),
            User_License_Plate[4:7].isalpha(), 
        
        ]
            
        if all(Requirements): # All function means that if all the requirements in the array are true then the Licence Plate is valid
            print("The Licence Plate", User_License_Plate + " is valid.")
            break
            
        else: # If all the requirements in the array isn't met then the Licence Plate is invalid
            print("The Licence Plate", User_License_Plate, "is not valid. Please check the format and try again.")


    User_Choice = input("Enter 'C' to continue checking for valid Licence Plates or 'M' to return to the main menu: ")  # Asks the user whether they want to search again or return to the main menu.
    while User_Choice.upper() != "C" and User_Choice.upper() != "M":  # Validates the user's choice.
        print("You've entered an invalid option, please try again") # Makes the user repeatedly input either "C" or "M" till either has been chosen
        User_Choice = input("Enter 'C' to continue or 'M' to return to the main menu: ")
    if (User_Choice.strip()).upper() == "C":  # Calls the search function again if C is selected.
        print("You've chosen to continue to check for valid Licence Plates.")
        User_Check_License()
    if (User_Choice.strip()).upper() == "M":  # Returns to the main menu if M is selected.
        print("You've chosen to return to the main menu.")
        User_Menu()

# 2  
def User_Car_Age():

    while True:

        User_License_Number = input("Please enter the Licence Plate without spaces of the car, you would like to check the age of: ") # Prompts user to enter a Licence Plate in order to determine the age of their car
        User_License_Number = User_License_Number.strip().upper()  # Convert the input to uppercase for consistency
    
        User_Region_Code = (User_License_Number[0:2]) # Extracting the first two characters of the license Plate to get the region code, in order to figure out whether the first 2 characters belongs to a valid Licence
    
        Found_Valid_Region = False

        for region in DVLA_Regions: # Looping through the list of DVLA regions to check if the region code is valid
                User_Region_Code in region[1] 
                Found_Valid_Region = True
                break

        Requirements = [ # Array that stores the requirements for a valid Licence Plate 
            
            Found_Valid_Region,
            len(User_License_Number) == 7,
            User_License_Number[0:2].isalpha(),
            User_License_Number[2:4].isdigit(),
            User_License_Number[4:7].isalpha(), 
        
        ]
            
        if all(Requirements): # All function means that if all requirements in the array are met then the Licence Plate is valid

            Car_Age = User_License_Number[2:4]
            if int(Car_Age) >= 50: # Calculates the age of vehicles with a 2-digit identifier of 50 or above
                Registration_Year = 2000 + (int(Car_Age) - 50)
                Car_Age_Calculation = 2026 - Registration_Year 
                print("Your vehicle is", Car_Age_Calculation, "years old registered between September", Registration_Year, "to February", str(Registration_Year + 1) + ".")
                break
                
            else: # Calculates the age of the vehicle that has the 2 digit identifier below 50
                Registration_Year = 2000 + int(Car_Age)
                Car_Age_Calculation = 2026 - Registration_Year 
                print("Your vehicle is", Car_Age_Calculation, "years old and registered between March to August", str(Registration_Year) + ".")
                break
            
        else: # Outputs that the Licence plate is invalid if the requirements in the array aren't met, forces the user to re-input a Licence Plate till a valid one is entered
            print(f"You've entered an invalid Licence Plate: {User_License_Number}, please try again.")

    User_Choice = input("Enter 'C' to continue checking the age of a car or 'M' to return to the main menu: ")  # Asks the user whether they want to search again or return to the main menu.
    while User_Choice.upper() != "C" and User_Choice.upper() != "M":  # Validates the user's choice.
        print("You've entered an invalid option, please try again") # Makes the user repeatedly input either "C" or "M" till either has been chosen
        User_Choice = input("Enter 'C' to continue or 'M' to return to the main menu: ")
    if (User_Choice.strip()).upper() == "C":  # Calls the search function again if C is selected.
        print("You've chosen to continue to check for how old a car is.")
        User_Car_Age()
    if (User_Choice.strip()).upper() == "M":  # Returns to the main menu if M is selected.
        print("You've chosen to return to the main menu.")
        User_Menu() 

# 3
def User_Registration_City():

    while True:
    
        User_Licence_City = input("Please enter the Licence Plate without spaces to check its registration city: ") # Prompting the user to enter a License Plate to check the registration 
        User_Licence_City = User_Licence_City.strip().upper()  # Convert the input to uppercase for consistency

        User_Region_Code = (User_Licence_City[0:2]) # Extracting the first two characters of the license Plate to get the region code, in order to figure out whether the first 2 characters belongs to a valid Licence

        Found_Valid_Region = False

        for region in DVLA_Regions: # Looping through the list of DVLA regions to check if the region code is valid
            if User_Region_Code in region[1]: 
                Found_Valid_Region = True
                Registration_City = region[2]
                break

        Requirements = [ # Array that stores the requirements for a valid Licence Plate 
                    
                    Found_Valid_Region,
                    len(User_Licence_City) == 7,
                    User_Licence_City[0:2].isalpha(),
                    User_Licence_City[2:4].isdigit(),
                    User_Licence_City[4:7].isalpha(), 
                
            ]
        
        if all(Requirements): # All function means that if all the requirements in the array are true then the Licence Plate is valid
            print("Your vehicle is registered in", Registration_City ,"your Licence Plate is also valid.")
            break

        else: # Outputs that the Licence plate is invalid if the requirements in the array aren't met, forces the user to re-input a Licence plate till a valid one is entered
            print(f"You've entered an invalid Licence Plate: {User_Licence_City}, please try again.")
            
    User_Licence_City = input("Press 'C' to continue, otherwise press 'M' to return to the Main Menu: ") # Allows the user to keep using a certain function in the program or return to main menu    
    while User_Licence_City.upper() != "C" and User_Licence_City.upper() != "M":
        print("You've entered an invalid option, please try again") # Makes the user repeatedly input either "C" or "M" till either has been chosen
        User_Licence_City = input("Press 'C' to continue, otherwise press 'M' to return to the Main Menu: ")
    if User_Licence_City.upper() == "C": # If the user inputs "C" then the program returns the user to the function
        print("You've chosen to continue to check the registration city of the car and whether the Licence Plate is valid.")
        User_Registration_City()
    if User_Licence_City.upper() == "M": # If the user inputs "M" then the program returns the user to the main menu
        print("You've chosen to exit the program, returning to the main menu...")
        User_Menu()

# 4
def User_Generate_License():
    
    Valid_Licence_Plate = [[  
    "AA17ABC",
    "AB18XYZ",
    "BD19DEF",
    "CA20GHI",
    "DA21JKL",
    "EA22MNO",
    "FA23PQR",
    "GA24STU",
    "HA25VWX",
    "KA17YZA",
    "LA18BCD",
    "MA19EFG",
    "NA20HIJ",
    "OA61KLM",
    "PA72NOP",
    "RA83QRS",
    "SA94TUV",
    "VA99WXY",
    "WA89ZAB",
    "YA76CDE" ]]
    for Licence in Valid_Licence_Plate:  # Looping through the list of valid License Plates to generate a random one
       print("A generated example of a valid Licence Plate:", random.choice(Licence))  # Displaying a randomly selected license Plate from the Valid Licence Plate list

    User_Licence_City = input("Press 'C' to continue, otherwise press 'M' to return to the Main Menu: ") # Allows the user to keep using a certain function in the program or return to main menu    
    while User_Licence_City.upper() != "C" and User_Licence_City.upper() != "M":
        print("You've entered an invalid option, please try again") # Makes the user repeatedly input either "C" or "M" till either has been chosen
        User_Licence_City = input("Press 'C' to continue, otherwise press 'M' to return to the Main Menu: ")
    if User_Licence_City.upper() == "C": # If the user inputs "C" then the program returns the user to the function
        print("You've chosen to continue generating Licence Plates.")
        User_Generate_License()
    if User_Licence_City.upper() == "M": # If the user inputs "M" then the program returns the user to the main menu
        print("You've chosen to exit the program, returning to the main menu...")
        User_Menu()

# 5
def User_Exit():
    
    User_Exit_Choice = input("Are you sure you want to exit? (Y/N): ")
    # Input validation to ensure the user enters either 'Y' or 'N'
    while User_Exit_Choice.upper() != "Y" and User_Exit_Choice.upper() != "N": # Neither Y or N
        print("You've entered an invalid option, please try again")
        User_Exit_Choice = input("Are you sure you want to exit? (Y/N): ")
    if User_Exit_Choice.upper() == "Y": # User has chosen to exit the program
        print("Thank you for using the DVLA Valid License Checker. Goodbye!")
        exit()
    elif User_Exit_Choice.upper() == "N": # User has chosen not to exit the program
        print("You've chosen not to exit the program, returning to the main menu...")
        User_Menu()

User_Menu() # Initial call for the program