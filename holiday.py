'''holiday calcultator taking users input for destination
number of nights staying and number of days car rental'''

# fixed variables
rental_cost = 70
hotel_per_night_cost = 100

# define hotel cost funtion
def hotel_cost():
    num_nights = int(input("How many nights are you wanting to stay for? "))
    hotel_cost = num_nights * hotel_per_night_cost
    print(f"Your hotel cost is: £{hotel_cost}")
    return hotel_cost

# define plane_cost function
def plane_cost():
    print("Select City destination.")
    print("1.New York")
    print("2.Washington")
    print("3.Quebec")
    print("4.Berlin")
    while True:
        try:
            city_flight = input("Enter choice(1/2/3/4): ")
            plane_cost = 0
            if city_flight == "1":
                plane_cost += 3000
            elif city_flight == "2":
                plane_cost += 2900
            elif city_flight == "3":
                plane_cost += 3100
            elif city_flight == "4":
                plane_cost += 300
            elif city_flight != ["1", "2", "3", "4"]: # goes back to input if wrong number is entered
                print("Wrong choice entered!")
                continue
            print(f"Your flight cost is: £{plane_cost}")
            return plane_cost
        except:
            break 
# define car_rental function
def car_rental():
    rental_days = int(input("How many day do you want to hire a car for? "))
    car_rental = rental_days * rental_cost
    print(f"Your car hire cost is: £{car_rental}")
    return car_rental

# define holiday total cost function
def holiday_cost():
    holiday_cost = plane_cost() + hotel_cost() + car_rental()
    print(f"Your total holiday cost would be £{holiday_cost}")

# main loop
holiday_cost()