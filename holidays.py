# This default functions added to clear the terminal and present the code on the top of the screen
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to calculate hotel cost based on the number of nights and city
def hotel_cost(num_nights, city):
    # Define hotel prices for different cities
    if city == "Madrid":
        price_per_night = 150
    elif city == "London":
        price_per_night = 200
    elif city == "Paris":
        price_per_night = 180
    elif city == "Moscow":
        price_per_night = 100
    else:
        # Default price if city is not recognized
        price_per_night = 100
    return num_nights * price_per_night

# Function to calculate plane cost based on the destination city
def plane_cost(city):
    # Define flight costs for different cities
    if city == "Madrid":
        return 200
    elif city == "London":
        return 300
    elif city == "Paris":
        return 260
    elif city == "Moscow":
        return 450
    else:
        # Default cost if city is not recognized
        return 400

# Function to calculate car rental cost based on the number of rental days and city
def car_rental(rental_days, city):
    # Define daily rental costs for different cities
    if city == "Madrid":
        daily_rental_cost = 50
    elif city == "London":
        daily_rental_cost = 70
    elif city == "Paris":
        daily_rental_cost = 60
    elif city == "Moscow":
        daily_rental_cost = 40
    else:
        # Default daily rental cost if city is not recognized
        daily_rental_cost = 50

    return rental_days * daily_rental_cost

# Function to calculate the total holiday cost including additional expenses
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Function to display costs in a formatted manner
def display_costs(num_nights, rental_days, city_flight, hotel, plane, car, vat, insurance, total):
    print("\nHOLIDAY COST:\n-----------------------------------------")
    print(f"Hotel cost for {num_nights} days\t\t£{hotel}")
    print(f"Car rental cost for {rental_days} days\t£{car}")
    print(f"Return flight to {city_flight}\t\t£{plane}")
    print("\nADDITIONAL EXPENSES:\n-----------------------------------------")
    print(f"20% VAT\t\t\t\t\t\t£{vat:.2f}")
    print(f"10% Travel Insurance\t\t\t£{insurance:.2f}")
    print("\nTOTAL HOLIDAY COST:\n-----------------------------------------")
    print(f"Total\t\t\t\t\t\t\t£{total + vat + insurance:.2f}")

# Welcome message
print(f'''{CLEAR} {CLEAR_AND_RETURN}                                  
                                Welcome to DREAM HOLIDAYS! 
      Get ready for an incredible holiday experience with our unbeatable quotes. 
      We're here to make your vacations extraordinary and budget-friendly.
      Please enter details of your holidays below and type the name of the city you wish to travel.
      
      Our Hot Flights this week:    * Madrid *
                                    * London *
                                    * Moscow *
                                    * Paris *
    ''')

# Set up while loop to ensure that the user enters correct inputs
while True:
    try:
        # Ask the user for the number of nights and rental days, converting inputs to integers
        # \n added for readability if user wants to compare multiple cities
        num_nights = int(input("\nNumber of nights: "))
        rental_days = int(input("Car rental days: "))
        # Use capitalize() function in case user types a city with lower case
        city_flight = (input("Destination name: ")).capitalize()

        # Check if the city exists
        if city_flight in ["Madrid", "London", "Paris", "Moscow"]:
            hotel = hotel_cost(num_nights, city_flight)
            plane = plane_cost(city_flight)
            car = car_rental(rental_days, city_flight)
            total = holiday_cost(hotel, plane, car)
            insurance = (total) * 0.13
            vat = (total) * 0.22
            # Display the costs
            display_costs(num_nights, rental_days, city_flight, hotel, plane, car, vat, insurance, total)
        else:
            print("\nSorry, but the city you entered is not recognized.")
            print("Please try again or contact our travel agent on 555 55 55 for further assistance.")

        # Ask the user if they want to start over
        start_over = input("\nDo you want to start over? Type 'Y' for Yes, 'N' for No: ").upper()
        if start_over != 'Y':
            print("Goodbye!!!")
            break  # Exit the loop if the user does not want to start over

    # Handle ValueError for invalid inputs
    except ValueError:
        print("Invalid input. Please enter correct details.")
