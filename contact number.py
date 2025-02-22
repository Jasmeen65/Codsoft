import json
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts found!")
        return
    print("\nContact List:")
    print("-" * 40)
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} | {contact['phone']}")

def add_contact(contacts):
    """Add a new contact."""
    name = input("\nEnter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        print("Contact added successfully!")
    else:
        print("Name and phone number are required.")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    query = input("\nEnter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    """Update an existing contact."""
    display_contacts(contacts)
    try:
        index = int(input("\nEnter the contact number to update: ")) - 1
        if 0 <= index < len(contacts):
            print("\nLeave fields blank to keep current values.")
            name = input(f"New Name ({contacts[index]['name']}): ").strip() or contacts[index]['name']
            phone = input(f"New Phone ({contacts[index]['phone']}): ").strip() or contacts[index]['phone']
            email = input(f"New Email ({contacts[index]['email']}): ").strip() or contacts[index]['email']
            address = input(f"New Address ({contacts[index]['address']}): ").strip() or contacts[index]['address']
            
            contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    """Delete a contact."""
    display_contacts(contacts)
    try:
        index = int(input("\nEnter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {deleted_contact['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the Contact Book app."""
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
