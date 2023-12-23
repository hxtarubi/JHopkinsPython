#Jude Yang
#7/28/21
#Total travel distance (2,400 miles)
#Total hours per day driving time (8 hours per day)
#Average miles per hour speed (60 miles per hour)
#Average miles per gallon for your car (25 miles per gallon)
#Average gas price per gallon ($2.50 per gallon)
#Motel cost per night (75.00 per night)

s = ("=" * 33)
#Border to keep results seperated

def motel_cost(totalTravel, travel_perDay, cost_perNight):
    return ((totalTravel/travel_perDay) * cost_perNight)

#The equation to figure out the total cost for the motels would be
#(total travel/miles per day) * cost per night

print("Total price for motels(in dollars):")
print(motel_cost(2400, 480, 75))
print(s)
print(" ")

def gas_cost(totalTravel, miles_perGallon, price_perGallon):
    return ((totalTravel/miles_perGallon) * price_perGallon)

#This function solves the amount of money the total amount of gas would cost
#by dividing the amount of miles they'll travel by the amount of miles they can
#travel per one gallon of gas, and multiplying the quotient by the cost per gallon.

print("Total price for gas(in dollars):")
print(gas_cost(2400, 25, 2.50))
print(s)
print(" ")

def total_cost(motel_cost, gas_cost):
    return (motel_cost + gas_cost)

print("Total cost(dollars):")
print(total_cost(375, 240))
print(s)

#This represents the total cost for everything





