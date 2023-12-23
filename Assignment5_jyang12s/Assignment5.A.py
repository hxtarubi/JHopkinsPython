#Jude Yang
#7/27/21

state = "States: %s %s %s"
state1 = "Pennsylvania"
state2 = "Virginia"
state3 = "Maryland"
print(state % (state1, state2, state3))
#Created a variable for all 3 states, and printed out the states' row.

print(" ")

population = "Population: %s     %s    %s"
PA_P = "12.81m"
VA_P = "8.4m"
MD_P = "6.052m"
print(population % (PA_P, VA_P, MD_P))
#Created a variable for the 3 populations, completing the population row.

print(" ")

area = "Area(miles): %s   %s   %s"
PA_A = "46,055"
VA_A = "42,707"
MD_A = "12,407"
print(area % (PA_A, VA_A, MD_A))
#Created the variables for the 3 areas, completing the chart.

space = (" " * 8)

print(" ")
print("-" * 50)

def density(population, area):
    return (population/area)
#Calculates the population density by dividing the population by the area.

def PDS():
    print("POPULATION DENSITY")
    print(" ")
    print("Pennsylvania")
    print(round(density(12810000, 46055)))
    print("=" * 20)
    print("Virginia")
    print(round(density(8400000, 42707)))
    print("=" * 20)
    print("Maryland")
    print(round(density(6052000, 12407)))
    print("=" * 20)
#Labels every state, and puts it's population density below it.
#Also seperates every state with a border
    
print(PDS())
