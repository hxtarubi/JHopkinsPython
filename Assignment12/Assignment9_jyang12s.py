#Jude Yang
#Assignment 12
#August 26, 2022


contacts_file = open("Contacts.txt", "r")
file_content = contacts_file.read()
contacts_list = file_content.split(",")
contacts_file.close()


#(A12)Read function first returns the contents of the file as a string. The split function then converst the string into a list which will be used in the program.

def Add_Contact(contact):
    if contact in contacts_list:
        duplicateContact = input("This contact has already been added to your list. Would you still like to add this contact?\nYes                 No\n")
        if duplicateContact == 'Yes' or duplicateContact == 'yes':
            contacts_list.append(contact)
        else:
            print("ok")
    else:
        contacts_list.append(contact)
    print("Successfully added contact:")
    print(" ")
    return(contacts_list)
#If the user wants to add a contact, they'll type out the name and it'll be added.
#(A12) If statement identifies whether the contact is already inside the list. If a contact has the same name as another contact in the list, the user will be prompted to choose whether to keep both contacts or to keep only one.


#If the user wants to add a contact, they'll type out the name and it'll be added.

def Delete_Contact(contact):
    if contact in contacts_list:
        contacts_list.remove(contact)
        print("Successfully deleted contact:")
        print(" ")
        return (contacts_list)
    else:
        return ("No such contact was found")


#If the user wants to delete a contact, they'll type the name and it'll be deleted.
#Note: If the contact isn't in the list, the following message will be printed.


def Update_Contact(contact):
    if contact in contacts_list:
        contacts_list.remove(contact)
        update = input("What would you like to change this contact to?")
        contacts_list.append(update)
        print("Successfully updated contact:")
        return (contacts_list)
    else:
        return ("That contact is not currently in your Contacts")


# If the user wants to update a contact, they'll type the contact and choose
# A different name for that contact, if the name isn't in the contacts
# A following message will tell them.

def Search_Contact(contact):
    if contact in contacts_list:
        return (contact)
    else:
        return ("This contact isn't in your contacts")


#If the user wants to search for a specific contact, they'll type the name
#And the contact will be printed out for them.

print("CONTACTS:")
print(" ")
contacts_list.remove('')
print("Currently your contacts include", contacts_list)
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
        print("Thank you for using this program")
        contacts_file = open("Contacts.txt", "w")
        for item in contacts_list:
            contacts_file.write(item + ",")
        contacts_file.close()
        #(A12)The write function then rewrites the file given to the most current and updated list.
        #Rather than writing the entire list, each contact is written into the file as an item in the list. This avoids further errors while reading the file.
        #(A12)Close function ensures that the changes made to the file were saved

        break
    # If the user chooses to stop using this program, they can enter the number
    # 5 in order to kill the program.

    else:
        print("This function is not avaliable or invalid")
    # If the user chooses a number other than 1-5, this message will notify them.

    print("~" * 40)
