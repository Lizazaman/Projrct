import os


FILENAME = "soil_nutrients.txt"

def initialize_file():
    
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            pass

def add_nutrient():
    
    crop_name = input("Enter crop name: ").strip()
    nitrogen = input("Enter nitrogen requirement (kg/ha): ").strip()
    phosphorus = input("Enter phosphorus requirement (kg/ha): ").strip()
    potassium = input("Enter potassium requirement (kg/ha): ").strip()

    with open(FILENAME, "a") as file:
        file.write(f"{crop_name},{nitrogen},{phosphorus},{potassium}\n")
    print("Nutrient record added successfully!")

def show_nutrients():
    
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No records found!")
                return
            print("\nCrop Name | Nitrogen (kg/ha) | Phosphorus (kg/ha) | Potassium (kg/ha)")
            print("-" * 50)
            for line in lines:
                crop_name, nitrogen, phosphorus, potassium = line.strip().split(",")
                print(f"{crop_name:10} | {nitrogen:16} | {phosphorus:18} | {potassium:15}")
    except FileNotFoundError:
        print("No data file found! Please add a record first.")

def search_nutrient():
    
    crop_name = input("Enter the crop name to search: ").strip().lower()
    found = False

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0].lower() == crop_name:
                    print(f"\nFound record: {record}")
                    found = True
                    break
        if not found:
            print("No record found for the specified crop!")
    except FileNotFoundError:
        print("No data file found! Please add a record first.")

def edit_nutrient():
    
    crop_name = input("Enter the crop name to edit: ").strip().lower()
    found = False
    updated_records = []

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0].lower() == crop_name:
                    print(f"Current record: {record}")
                    nitrogen = input("Enter new nitrogen requirement (kg/ha): ").strip()
                    phosphorus = input("Enter new phosphorus requirement (kg/ha): ").strip()
                    potassium = input("Enter new potassium requirement (kg/ha): ").strip()
                    updated_records.append(f"{record[0]},{nitrogen},{phosphorus},{potassium}\n")
                    found = True
                else:
                    updated_records.append(line)

        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_records)
            print("Record updated successfully!")
        else:
            print("No record found for the specified crop!")
    except FileNotFoundError:
        print("No data file found! Please add a record first.")

def delete_nutrient():
    
    crop_name = input("Enter the crop name to delete: ").strip().lower()
    found = False
    updated_records = []

    try:
        with open(FILENAME, "r") as file:
            for line in file:
                record = line.strip().split(",")
                if record[0].lower() == crop_name:
                    found = True
                    print(f"Deleted record: {record}")
                else:
                    updated_records.append(line)

        if found:
            with open(FILENAME, "w") as file:
                file.writelines(updated_records)
            print("Record deleted successfully!")
        else:
            print("No record found for the specified crop!")
    except FileNotFoundError:
        print("No data file found! Please add a record first.")

def menu():

    while True:
        print("\nSoil Nutrient Management System")
        print("1. Add Nutrient Record")
        print("2. Show All Records")
        print("3. Search for a Record")
        print("4. Edit a Record")
        print("5. Delete a Record")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_nutrient()
        elif choice == "2":
            show_nutrients()
        elif choice == "3":
            search_nutrient()
        elif choice == "4":
            edit_nutrient()
        elif choice == "5":
            delete_nutrient()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


initialize_file()
menu()