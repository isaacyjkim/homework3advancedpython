from Contact import Contact
from ContactList import ContactList
from Node import Node
def main():
    contacts = ContactList()
    str = ""
    str += "1.) Add Contact \n2.) Remove Contact\n3.) Change phone number\n4.) Print contacts\n5.) Quit"
    while True:
        print(str)
        inp = input(">>> ")
        if (inp=='5'):
            break
        elif (inp =='1'):
            name = input("Enter a name: ")
            phone = input("Enter a phone number: ")
            contacts.add(name,phone)
        elif (inp =='2'):
            name = input("Enter a name to remove: ")
            contacts.remove(name)
        elif (inp =='4'):
            print(contacts)







main()