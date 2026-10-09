from inventory import *
from borrowing import *
from reports import *


def show(items):
    for r in items:
        print(r)


while True:
    print("\n1.List  2.Add  3.Search  4.Category  5.Borrow  6.Return  7.Records  8.Report  9.Exit")
    choice = input("Choose: ")

    if choice == "1":
        show(list_resources())

    elif choice == "2":
        name = input("Name: ")
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        print(add_resource(name, category, quantity))

    elif choice == "3":
        show(search_resources(input("Search: ")))

    elif choice == "4":
        show(filter_category(input("Category: ")))

    elif choice == "5":
        name = input("Resource: ")
        fellow = input("Fellow: ")
        quantity = int(input("Quantity: "))
        print(borrow_resource(name, fellow, quantity))

    elif choice == "6":
        name = input("Resource: ")
        fellow = input("Fellow: ")
        quantity = int(input("Quantity: "))
        print(return_resource(name, fellow, quantity))

    elif choice == "7":
        show(list_borrow_records())

    elif choice == "8":
        print(generate_report())
        print("Low stock:", low_stock_resources())
        print("Most borrowed:", most_borrowed_resource())

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")