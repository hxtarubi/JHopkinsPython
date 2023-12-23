#Assignment 10
#Jude Yang
#7/20/22

#Most of the comments are for future reference so I don't end up making the same mistakes.

import random

class DiceGame:
    def __init__(self):
        self.dieOne = Die('0', '0')
        self.dieTwo = Die('0', '0')
        #Both die starts with the value 0 so that the number accurately
        #determines the face value and the face of the die.
        #By placing "self" in front of dieOne and dieTwo, both dice are assigned
        #to the DiceGame class
        
    def play(self):
        while True:
            self.dieOne.roll()
            self.dieTwo.roll()
            print(" ")
            playAgain = input("do you want to play again?\nYes                No\n")
            #Assignment Operator - Assigns a value to the variable.
            if playAgain == "Yes" or playAgain == "yes":
                #Equality Operator - Returns a true or false value (Used mostly in
                #a if statement.)
                pass
            elif playAgain == "No" or playAgain == "no":
                break
            else:
                break
#The program rolls both die, then asks the user if they want to play again.
#if the user wants to play again, the while loop will reroll the die
#if not, the break function will stop the while loop
            
            
            
        
class Die:
    def __init__ (self, objFace, objFaceValue):
        self.face = objFace
        self.faceValue = objFaceValue
        #Creates the face and face value attributes for the Die class.

    def roll(self):
        number = random.randint(1, 6)
        objFaceValue = number
        if objFaceValue == 1:
            print (" -------\n|       |\n|   o   |\n|       |\n -------")
        elif objFaceValue == 2:
            print (" -------\n|  o    |\n|       |\n|    o  |\n -------")
        elif objFaceValue == 3:
            print (" -------\n|  o    |\n|   o   |\n|    o  |\n -------") 
        elif objFaceValue == 4:
            print (" -------\n|  o  o |\n|       |\n|  o  o |\n -------")
        elif objFaceValue == 5:
            print (" -------\n|  o  o |\n|   o   |\n|  o  o |\n -------")
        elif objFaceValue == 6:
            print (" -------\n|  o  o |\n|  o  o |\n|  o  o |\n -------")
        #Using the random module, an integer between 1-6 is chosen.
        #Using if statements, the number is then used to create the face of the die 

        print(" ")
        #line break
        
        print("Face Value:" + str(objFaceValue))
        print(" ")
        #objFaceValue is an integer and so assigned to a string
        #Plus operator links the two strings together.  
        #The number is also used to print out the face value of the die


game = DiceGame()
#Creates the DiceGame object (A class doesn't run by itself & needs to be created)
#DiceGame() calls the init method which is the constructor.
game.play()
