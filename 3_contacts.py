class ContactList(list):
    def search(self, name):
        'Return all contacts that contain the search value in their name.'
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send " "'{}' order to '{}'".format(order, self.name))

c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
s = Supplier("Sup Plier", "supplier@example.net")

print(c1.name, c1.email, s.name, s.email)
print('====')
print(s.order("I need pliers"))
print('====')
print([c.name for c in Contact.all_contacts.search('John')])
