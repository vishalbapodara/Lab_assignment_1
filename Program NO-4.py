# Initialize an empty list to store employee names
EMPNAME = []

# Function to add a name to the list
def add_employee(name):
    EMPNAME.append(name)
    print(f"Employee '{name}' added.")

# Function to remove a name from the list
def remove_employee(name):
    if name in EMPNAME:
        EMPNAME.remove(name)
        print(f"Employee '{name}' removed.")
    else:
        print(f"Employee '{name}' not found in the list.")

# Function to append a name to the list
def append_employee(name):
    EMPNAME.append(name)
    print(f"Employee '{name}' appended to the list.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nEMPNAME List:", EMPNAME)
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Append Employee")
        

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter employee name to add: ")
            add_employee(name)
        elif choice == '2':
            name = input("Enter employee name to remove: ")
            remove_employee(name)
        elif choice == '3':
            name = input("Enter employee name to append: ")
            append_employee(name)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
