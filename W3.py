#TASK 3s
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self, filename):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    name, phone, email = line.strip().split(',')
                    self.contacts.append(Contact(name, phone, email))
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name} - {contact.phone} - {contact.email}")

    def edit_contact(self):
        self.view_contacts()
        choice = int(input("Enter the number of the contact to edit: ")) - 1
        contact = self.contacts[choice]
        print("1. Edit name")
        print("2. Edit phone number")
        print("3. Edit email")
        option = int(input("Enter your choice: "))
        if option == 1:
            contact.name = input("Enter new name: ")
        elif option == 2:
            contact.phone = input("Enter new phone number: ")
        elif option == 3:
            contact.email = input("Enter new email: ")
        self.save_contacts()

    def delete_contact(self):
        self.view_contacts()
        choice = int(input("Enter the number of the contact to delete: ")) - 1
        del self.contacts[choice]
        self.save_contacts()

def main():
    manager = ContactManager('contacts.txt')
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Quit")
        option = int(input("Enter your choice: "))
        if option == 1:
            manager.add_contact()
        elif option == 2:
            manager.view_contacts()
        elif option == 3:
            manager.edit_contact()
        elif option == 4:
            manager.delete_contact()
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()