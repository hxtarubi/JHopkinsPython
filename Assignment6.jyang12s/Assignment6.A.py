#Jude Yang
#7/29/21

g = input ("Enter the amount of people that will be staying:")
print(" ")
print("=" * 40)
n = input ("Enter the amount of nights you'll be staying:")
print(" ")
#The user will input a number to represent the amount of guests, and nights
#they'll be staying. The number of guests will be saved in the variable
#guest_amount, while the number of nights will be saved in the variable
#night_amount

guest_amount = int(g)
night_amount = int(n)

if guest_amount == 1:
    print("You'll be staying in a Single Occupancy Room.")
    single_cost = night_amount * 50
    print('''Your total will be $''', single_cost)
#If there's only one guest, they will be prompted to choose the Single Occupancy
#Room, and the cost for their stay will be calculated.

elif guest_amount == 2:
    print("You'll be staying in a Double Occupancy Room.")
    double_cost = night_amount * 75
    print('''Your total will be $''', double_cost)
#If there's two guests, they would choose the Double Occupancy Room, and
#be given their price.

elif guest_amount >= 3:
    r = input ("Please choose between a Penthouse and Deluxe room.")
    if r == "Penthouse" or r == "penthouse":
        print("You'll be staying in a Penthouse room.")
        pent_cost = night_amount * 300
        print('''Your total will be $''', pent_cost)

    elif r == "Deluxe" or r == "deluxe":
        print("You'll be staying in a Deluxe room.")
        deluxe_cost = night_amount * 200
        print('''Your total will be $''', deluxe_cost)

    else:
        print("That is not a room, choose again")
#If there are more than 2 guests, they will get to decide between the Penthouse
#Room and the Deluxe Room. Based off of their choice, the price will be calculated.
        
else:
    print("Invalid")
            
              
    
    



