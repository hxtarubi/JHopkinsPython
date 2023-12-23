#Jude Yang
#7/29/21

#Up to 50 balloons - $1.00 each
#Over 50 and up to 100 - $0.50 each additional balloon
#Over 100 - $0.25 each additional balloon

total = input ("Enter the amount of balloons to be purchased:")
print(" ")
print("The amount of balloons you will buy will be: ", total)
print(" ")
print("=" * 40)
print("The cost is:")

balloon_amount = int(total)
#The user will input a number to represent the amount of balloons they'll purchase
#which will then be saved in the variable balloon_amount.

if balloon_amount <= 50 and balloon_amount > 0:
    balloon_cost = balloon_amount * 1
    print(balloon_cost)
#This if statement prints out the total cost of the balloons by multiplying them
#by one since they cost a dollar each (when you buy less than 50).    

elif balloon_amount > 50 and balloon_amount <= 100:
    print(50 + ((balloon_amount - 50) * 0.5))
#This elif statement prints out the total cost by adding 50 to the
#product of the leftover balloons multiplied by 0.5. This is because
#since you have more than 50 balloons, you'll have to spend $50 on the first fifty
#and then pay the $0.5 per leftover balloons.


elif balloon_amount >100:
    print((balloon_amount - 100) * 0.25 + 75)
#This elif statement follows the same logic as the last elif statement
#as since you have more than 100 balloons, you'll have to spend $50 on the first
#50 balloons, and then $25 on the next 50 balloons, multiplying 0.25 with
#the leftover balloons.

else:
    print("Invalid")
