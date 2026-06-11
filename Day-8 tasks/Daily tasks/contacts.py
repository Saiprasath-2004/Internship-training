
contacts = {}

def add_contact(name,phone):
    contacts[name]=phone
    print(f"{name} added successfully")

def find_contact(name):
    try:
        print(f"{name} : {contacts[name]}")
    except KeyError:
        print("Contact not found")


def list_contacts():
    print("\n Contacts:")

    if len(contacts)== 0:
        print("No contacts available")
        return
    
    for name, phone in contacts.items():
        print(name, "-", phone)