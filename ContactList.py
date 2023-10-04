from Node import Node
from Contact import Contact
class ContactList:

    def __init__(self):
        self._head = None


    def add(self,name,new_number):
        """Creates new_contact and new_node objects to add"""
        new_contact = Contact(name,new_number)
        new_node = Node(new_contact,self._head)
        self._head = new_node

    def remove(self,name):
        probe = self._head
        while probe is not None:
            if (probe._data._name==name):
                break










    def __str__(self):
        str = ""
        probe = self._head
        while probe is not None:
            str +=(probe._data._name)
            str +=": "+ (probe._data._phone_number) + "\n"
            probe = probe._next
        return str
