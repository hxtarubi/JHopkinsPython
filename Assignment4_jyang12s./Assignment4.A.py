#Jude Yang
#7/26/21

print("Model A")
state = "States: %s %s %s"
state1 = "Pennsylvania"
state2 = "Virginia"
state3 = "Maryland"
print(state % (state1, state2, state3))
#Created a variable for all 3 states, and printed out the states' row.

print(" ")

population = "Population: %s     %s    %s"
VA_P = "12.81m"
NY_P = "8.4m"
MD_P = "6.052m"
print(population % (VA_P, NY_P, MD_P))
#Created a variable for the 3 populations, completing the population row.

print(" ")

area = "Area(miles): %s   %s   %s"
PA_A = "46,055"
VA_A = "42,707"
MD_A = "12,407"
print(area % (PA_A, VA_A, MD_A))
#Created the variables for the 3 areas, completing the chart.

#The following line of code will be the same but with the variable values'
#of Virginia changed.

print(" ")
print(" ")
print(" ")
print("Model B")
state = "States: %s %s %s"
state1 = "Pennsylvania"
state2 = "Virginia"
state3 = "Maryland"
print(state % (state1, state2, state3))

print(" ")

population = "Population: %s     %s    %s"
PA_P = "12.81m"
VA_P = "4.8m"
MD_P = "6.052m"
print(population % (PA_P, VA_P, MD_P))
#Due to the pandemic, around half the populaiton of Virginia had died.
#In a realistic situation, all the populations listed would have decreased,
#but it was told to only change Virginia's variables.

print(" ")

area = "Area(miles): %s   %s   %s"
PA_A = "46,055"
VA_A = "42,707"
MD_A = "12,407"
print(area % (PA_A, VA_A, MD_A))
