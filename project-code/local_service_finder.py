import pickle
import os

DATA_FILE = "services.pkl"
CREDENTIALS_FILE = "credentials.pkl"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as file:
        services = pickle.load(file)
else:
    services = []

if os.path.exists(CREDENTIALS_FILE):
    with open(CREDENTIALS_FILE, "rb") as file:
        admin_credentials = pickle.load(file)
else:
    admin_credentials = {"admin": "admin123"}

def save_credentials():
    with open(CREDENTIALS_FILE, "wb") as file:
        pickle.dump(admin_credentials, file)

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Admin Login")
        print("2. Admin Sign-Up")
        print("3. User")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            admin_sign_up()
        elif choice == "3":
            user_menu()
        elif choice == "4":
            with open(DATA_FILE, "wb") as file:
                pickle.dump(services, file)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def admin_sign_up():
    print("\n--- Admin Sign-Up ---")
    while True:
        new_username = input("Enter a new admin username: ").strip()
        if new_username in admin_credentials:
            print("Username already exists! Please choose a different username.")
        else:
            new_password = input("Enter a new admin password: ").strip()
            confirm_password = input("Confirm password: ").strip()
            if new_password == confirm_password:
                admin_credentials[new_username] = new_password
                save_credentials()
                print(f"Admin '{new_username}' registered successfully!")
                break
            else:
                print("Passwords do not match! Please try again.")

def admin_login():
    print("\n--- Admin Login ---")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if username in admin_credentials and admin_credentials[username] == password:
        print("Login successful!")
        admin_menu()
    else:
        print("Invalid credentials!")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Service")
        print("2. View All Services")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Add Service ---")
            work = input("Enter type of work (e.g., plumber): ").strip()
            location = input("Enter location: ").strip()
            contact = input("Enter contact number: ").strip()
            services.append({"work": work, "location": location, "contact": contact})
            print("Service added successfully!")
        elif choice == "2":
            print("\n--- View All Services ---")
            if services:
                for idx, service in enumerate(services, start=1):
                    print(f"{idx}. Work: {service['work']}, Location: {service['location']}, Contact: {service['contact']}")
            else:
                print("No services available.")
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. Search for a Service")
        print("2. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Search Service ---")
            work = input("Enter type of work you need: ").strip().lower()
            location = input("Enter location: ").strip().lower()
            found_services = [s for s in services if s['work'].lower() == work and s['location'].lower() == location]
            if found_services:
                for service in found_services:
                    print(f"Found: {service['work']} in {service['location']} (Contact: {service['contact']})")
            else:
                print("No matching services found.")
        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()