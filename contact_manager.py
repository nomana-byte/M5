"""A simple contact manager with exception handling."""

contacts = {}


class DuplicateContactError(Exception):
    """Raised when a contact name already exists."""


def add_contact(name, phone):
    """Add a new contact to the dictionary."""
    if name in contacts:
        raise DuplicateContactError(
            f"Contact '{name}' already exists."
        )

    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Find a contact and return the phone number or None."""
    try:
        phone = contacts[name]
        print(f"{name}: {phone}")
        return phone
    except KeyError:
        print("Contact not found.")
        return None


def delete_contact(name):
    """Delete a contact if it exists."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")


def main():
    """Display the contact manager menu and process choices."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()

            if not name or not phone:
                print("Name and phone number cannot be empty.")
                continue

            try:
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(error)

        elif choice == 2:
            name = input("Enter name to find: ").strip()
            find_contact(name)

        elif choice == 3:
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == 4:
            print("Exiting Contact Manager.")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
