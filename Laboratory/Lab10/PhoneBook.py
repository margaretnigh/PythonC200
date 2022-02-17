
from Contact import Contact
class PhoneBook:
    def __init__(self):
        """
        The phonebook keeps track of all contacts. This class is an example of 
        interacting with other classes a coder will make. 
        Instance variables provided for this constructor.
        """
        self.contact_list = [ ]
        self.count = 0
    
    def addContact(self, c):
        """
        Given a contact, determine if you are given a dictionary or an instance of 
        a Contact class. Handle the adding to our phone book appropriately and 
update the counter.
        If you are given a dictionary, assume that a dictionary has the following 
keys 
        (and the values are in the correct format):
        - name
        - number
        - email
        - birthday
        NOTE: Why do we have to manually update the counter?
        """
        if isinstance(c,Contact):
            self.contact_list.append(c)
            self.count += 1
        elif isinstance(c,dict):
            n = c["name"]
            num = c["number"]
            e = c["email"]
            b = c["birthday"]
            con = Contact(n,num,e,b)
            self.contact_list.append(con)
            self.count += 1

    
    def getContactCount(self):
        """
        Returns the number of contacts stored in the 
        """
        return self.count
    
    def findContact(self, lName):
        """
        Given a last name, find the contact(s) and return the contact information. 
        Will be a list. 
        """
        temp = []
        for i in self.contact_list:
            if i.last == lName:
                temp.append(i)
        return temp

    def groupChat(self, message):
        """
        Send a message to every contact in the phonebook
        """
        for i in self.contact_list:
            i.sendtext()

    def __str__(self):
        """
        Returns a string representation of the phonebook class. 
        The output will be
        > Phone Book: #
        Where # is the number of contacts in the phonebook. 
        """
        return f"Phone Book: {self.getContactCount()}"
    
