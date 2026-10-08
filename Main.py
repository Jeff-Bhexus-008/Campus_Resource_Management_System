from inventory import add_resource, list_resources, search_resources, filter_category
from borrowing import borrow_resource, return_resource
from reports import report


resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {
    "F001": "Ada", 
    "F002": "John", 
    "F003": "Grace"
}
borrow_records = []

while True:
    print("\n--- CAMPUS RESOURCE MANAGEMENT SYSTEM ---")
    print("1. Add Resource")
    print("2. List Resources")
    print("3. Borrow Resource")
    print("4. Return Resource")
    print("5. Search Resource")
    print("6. Filter by Category")
    print("7. Generate Report")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_resource(resources)

    elif choice == "2":
        list_resources(resources)

    elif choice == "3":
        borrow_resource(resources, fellows, borrow_records)

    elif choice == "4":
        return_resource(resources, fellows, borrow_records)

    elif choice == "5":
        search_resources(resources)

    elif choice == "6":
        filter_category(resources)

    elif choice == "7":
        report(resources)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Choose 1-8.")