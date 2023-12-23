#Jude Yang
#Final Project
#September 7, 2022

inventory = open("booklist.txt", "r")
view_file = inventory.readlines()
inventory.close()
#Opens the file containing all the books and their information.
#Readlines is used later to organize and print the book information.

cart = open("cart.txt", "r+")
view_cart = cart.read()
cart_list = view_cart.split(",")
cart.close()
#Opens the file that will be used to save the books that the user wants.
#The user's input is then saved as a list, using the split funciton to seperate all the book IDs.

def displayMenu():
    print(" ")
    print("ABC Book Store")
    print(" ")
    print("1 - View the Books on Sale")
    print(" ")
    print("2 - Add a Book into Your Cart")
    print(" ")
    print("3 - Show items in Your Cart")
    print(" ")
    print("4 - Remove a Book from Your Cart:")
    print(" ")
    print("5 - Checkout")
    print(" ")
    print("6 - Leave")
    print("=" * 40)
    #Basic menu screen that gives the user options in the book store.
    
def displayBook():
    x = 0
    while x < 5:
        book = view_file[x].split(",")
        print("Item Number: " + book[0])
        print("Title: " + book[1])
        print("Author: " + book[2])
        print("Genre: " + book[3])
        print("Price: $" + book[4])
        x += 1
    print("=" * 40)
    #The while loop organizes the 5 items in the list (view_file) until the x value is equal to 5. The x value increases by one every time the while loop functions, hence it will stop when all 5 items are organized.
    #All the items represents a book containing it's general information. Since all the books have 5 values (Item number/ID, title, author, genre, & price), the index function is used to seperate the values to print in order.

bookID = {'1000' : 'Science: A Visual Encyclopedia',
          '1001' : 'My First Human Body Book',
          '1002' : 'The Runaway Children',
          '1003' : 'The Tuscan child',
          '1004' : 'Learning Python'}
#The bookID map is used to transform the bookID into it's corresponding book.
#The ID being the key while the book title is the value.


bookPrice = {'1000' : '23.99',
             '1001' : '3.99',
             '1002' : '3.99',
             '1003' : '9.99',
             '1004' : '61.99'}
#The bookPrice map is used to transform the bookID into it's corresponding price,
#The ID being the key while the price of the book is the value.

def addToCart():
    addBook = input("Write the ID of the book that you would like to add to your cart:\n")
    if addBook == '1000' or addBook == '1001' or addBook == '1002' or addBook == '1003' or addBook == '1004':
        print(bookID[addBook])
        #The user input is taken into an if statement which checks if the book ID matches with the one on the file.
        #If it is, the program prints the book title using the bookID map.
        confirm = input("Is this the book you would like to add to cart?\nYes                              No\n")
        if confirm == 'Yes' or confirm == 'yes':
              cart_list.append(addBook)
        else:
            print("Please choose a different book.")
        #The user is told to confirm whether the book is correct, and the book is added to the cart_list if the input is yes.
        #Otherwise the user is prompted to choose a different book.
    else:
        print("That is not a book currently in shop. Please choose a different book.")
        #If the user input does not match with the book IDs on the file, they are prompted to choose a different book.
        
def viewCart():
    print("Your cart currently contains:")
    print(" ")
    x = 0
    while x < len(cart_list):
        print(bookID[cart_list[x]])
        x += 1
    print("=" * 40)
    #The while loop runs until the x value is lower than the amount of items in the list. The x value is increased by one every time the while loop functions.
    #The x value also represents the index of the cart_list, printing all the book titles that are in the list using the bookID map.

def removeFromCart():
    removeBook = input("Write the ID of the book that you would like to remove from your cart:\n")
    if removeBook in cart_list:
        print(bookID[removeBook])
        #The if statement checks if the user input is a part of the cart_list.
        #If it is, than the bookID map is used in order to print the title of the book
        confirm = input("Is this the book you would like to remove from your cart?\nYes                              No\n")
        if confirm == 'Yes' or confirm == 'yes':
              cart_list.remove(removeBook)
              #The user is prompted to confirm whether that is the book that they would like to remove from their cart.
              #If the user input is yes or Yes, then the remove function is used to delete the item from the list,
        else:
            print("Please choose a different book.")
            #Otherwise, the user is prompted to choose a different book.
    else:
        print("That is not a book currently in your Cart. Please choose a different book.")
        #If the book ID does not match with the ones that are in the list, then the user is prompted to choose a different book.
        

def checkout():
    x = 0
    #x value represents the total price value. Therefore it starts at 0.
    y = 0
    #y value represents the index number of the cart_list, increasing by one every time the for loop functions.
    for i in cart_list:
        x += (float(bookPrice[cart_list[y]]))
        y += 1
        #For loop runs for every item in the cart_list, using the bookPrice map to convert the book's ID into the price.
        #The price is then added to x.
        #The y value increases by 1 to get all the items in the cart_list.
    print("The total price is: $", round(x, 2))

class Inventory():
    pass

class Cart():
    pass

class Book():
    pass

    
        
    
cart_list.remove('')
#Because the cart_list begins with no value, the list contains the item ''. This is unnecessary in the code and is promptly deleted from the list.

while True:
    
    print(" ")
    
    displayMenu()
    #The menu is displayed to the user.
    
    action = input("Type what action you'd like to complete:")
    print(" ")
    #The user is prompted to complete an action.

    if int(action) == 1:
        print("Here are the books on sale:\n")
        displayBook()
        #display the books

    if int(action) == 2:
        addToCart()
        #add book to cart

    if int(action) == 3:
        viewCart()
        #view the user's current cart

    if int(action) == 4:
        removeFromCart()
        #remove a book from cart

    if int(action) == 5:
        checkout()
        confirmPurchase = input("Are you sure you'd like to checkout?\nYes                          No\n")
        #User is prompted to confirm their purchase.
        if confirmPurchase == 'Yes' or confirmPurchase == 'yes':
            print("Thank you for shopping at ABC Bookstore")
            cart_list.clear()
            #If the user input is yes or Yes, then the cart_list is cleared of all it's items.
        else:
            print("Your purchase was cancelled")
            #Otherwise the user is told that their purchase was cancelled.
        
    if int(action) == 6:
        save = input("Would you like to update your Cart\nYes                              No\n")
        #The user is prompted to choose whether they'd like to save their current cart.
        if save == 'Yes' or save == 'yes':
            cart = open("cart.txt", "w") 
            for item in cart_list:
                cart.write(item + ",")
                #If the user input is yes or Yes, all the items in the cart_list is added to the file using the write function.
            cart.close()
            break
        else:
            break

    
        
        
        
        


    
