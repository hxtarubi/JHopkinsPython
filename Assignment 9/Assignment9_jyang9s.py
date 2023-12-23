#Jude Yang
#Assignment 9
#August 18, 2021

list = []

print("CONTACTS:")
print(" ")
print("1 - Add Contatct")
print(" ")
print("2 - Delete Contact")
print(" ")
print("3 - Update Contact")
print(" ")
print("4 - Search Contact")
print(" ")
print("5 - Leave")
print("=" * 40)
#Contacts page that lists the instructions.

def Add_Contact(contact):
    list.append(contact)
    print("Successfully added contact:")
    print(" ")
    return(list)
#If the user wants to add a contact, they'll type out the name and it'll be added.

def Delete_Contact(contact):
    if contact in list:
        list.remove(contact)
        print("Successfully deleted contact:")
        print(" ")
        return(list)
   
    else:
        return("No such contact was found")
#If the user wants to delete a contact, they'll type the name and it'll be deleted.
#Note: If the contact isn't in the list, the following message will be printed.
    

def Update_Contact(contact):
    if contact in list:
        list.remove(contact)
        update = input("What would you like to change this contact to?")
        list.append(update)
        print("Successfully updated contact:")
        return(list)
    
    else:
        return("That contact is not currently in your Contacts")
#If the user wants to update a contact, they'll type the contact and choose
# A different name for that contact, if the name isn't in the contacts
# A following message will tell them.

def Search_Contact(contact):
    if contact in list:
        return(contact)
    else:
        return("This contact isn't in your contacts")
#If the user wants to search for a specific contact, they'll type the name
#And the contact will be printed out for them.
        

while True:
    print(" ")
    action = input("Please choose what action you want to complete:")
    print(" ")
    
    if int(action) == 1:
        contact = input("Who would you like to add to your contacts?:")
        print(Add_Contact(contact))

    elif int(action) == 2:
        contact = input("Who would you like to delete from your contacts?:")
        print(Delete_Contact(contact))

    elif int(action) == 3:
        contact = input("What contact would you like to update?:")
        print(Update_Contact(contact))

    elif int(action) == 4:
        contact = input("What contact would you like to search for?:")
        print(Search_Contact(contact))
        
    elif int(action) == 5:
        break
    #If the user chooses to stop using this program, they can enter the number
    #5 in order to kill the program.

    else:
        print("This function is not avaliable or invalid")
    #If the user chooses a number other than 1-5, this message will notify them.

    print("~" * 40)


    
    
    




