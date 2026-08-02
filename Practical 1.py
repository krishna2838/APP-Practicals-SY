class LibraryResource:
    def __init__(self, item_id, title, creator):
        self.item_id = item_id
        self.title = title
        self.creator = creator
        self.is_checked_out = False

    def show_info(self):
        availability = "Checked Out" if self.is_checked_out else "On Shelf"
        print(f"[Item ID: {self.item_id}] {self.title} by {self.creator} | Status: {availability}")


class LibraryMember:
    def __init__(self, member_id, full_name):
        self.member_id = member_id
        self.full_name = full_name
        self.current_loans = []

    def show_info(self):
        print(f"Member Name: {self.full_name} (ID: {self.member_id})")
        if self.current_loans:
            print(f"-> Active Loans: {', '.join(self.current_loans)}")
        else:
            print("-> Active Loans: None")


class CatalogSystem:
    def __init__(self):
        self.inventory = {}
        self.members = {}

    def insert_resource(self, item_id, title, creator):
        if item_id in self.inventory:
            print(f"Warning: Item ID {item_id} already exists in the catalog.")
            return
            
        self.inventory[item_id] = LibraryResource(item_id, title, creator)
        print(f"Success: '{title}' has been added to the catalog.")

    def enroll_member(self, member_id, full_name):
        if member_id in self.members:
            print(f"Warning: Member ID {member_id} is already in use.")
            return
            
        self.members[member_id] = LibraryMember(member_id, full_name)
        print(f"Success: Member '{full_name}' has been enrolled.")

    def process_checkout(self, member_id, item_id):
        member = self.members.get(member_id)
        resource = self.inventory.get(item_id)

        if not member:
            print("Error: Member ID not recognized.")
            return
        if not resource:
            print("Error: Item ID not found in catalog.")
            return
        if resource.is_checked_out:
            print(f"Notice: '{resource.title}' is currently checked out by someone else.")
            return

        resource.is_checked_out = True
        member.current_loans.append(resource.title)
        print(f"Transaction Complete: {member.full_name} checked out '{resource.title}'.")

    def process_return(self, member_id, item_id):
        member = self.members.get(member_id)
        resource = self.inventory.get(item_id)

        if not member or not resource:
            print("Error: Invalid Member ID or Item ID provided.")
            return

        if resource.title in member.current_loans:
            resource.is_checked_out = False
            member.current_loans.remove(resource.title)
            print(f"Transaction Complete: {member.full_name} returned '{resource.title}'.")
        else:
            print("Error: This item is not in this member's current loans.")

    def print_inventory(self):
        print("\n--- Current Inventory ---")
        if not self.inventory:
            print("The catalog is completely empty.")
            return
        for item in self.inventory.values():
            item.show_info()

    def print_members(self):
        print("\n--- Enrolled Members ---")
        if not self.members:
            print("No members are currently enrolled.")
            return
        for member in self.members.values():
            member.show_info()
            print("-" * 20)


def run_application():
    system = CatalogSystem()

    # Helper functions for the interactive menu
    def action_add_book():
        i_id = input("Enter New Item ID: ")
        title = input("Enter Title: ")
        creator = input("Enter Author: ")
        system.insert_resource(i_id, title, creator)

    def action_add_member():
        m_id = input("Enter New Member ID: ")
        name = input("Enter Member Full Name: ")
        system.enroll_member(m_id, name)

    def action_checkout():
        m_id = input("Enter Member ID: ")
        i_id = input("Enter Item ID: ")
        system.process_checkout(m_id, i_id)

    def action_return():
        m_id = input("Enter Member ID: ")
        i_id = input("Enter Item ID: ")
        system.process_return(m_id, i_id)

    # Dictionary-based menu dispatcher (replaces the long if/elif chain)
    menu_options = {
        "1": action_add_book,
        "2": action_add_member,
        "3": action_checkout,
        "4": action_return,
        "5": system.print_inventory,
        "6": system.print_members
    }

    while True:
        print("\n=== Library Management Dashboard ===")
        print("1. Add New Resource")
        print("2. Enroll New Member")
        print("3. Process Checkout")
        print("4. Process Return")
        print("5. View All Resources")
        print("6. View All Members")
        print("7. Close Application")

        user_selection = input("Choose an option (1-7): ")

        if user_selection == "7":
            print("Closing application. Goodbye!")
            break

        # Execute the chosen function, or show an error if invalid
        selected_action = menu_options.get(user_selection)
        if selected_action:
            selected_action()
        else:
            print("Invalid input. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    run_application()