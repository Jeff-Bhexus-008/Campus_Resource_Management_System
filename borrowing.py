from inventory import resources


borrow_records = []


def borrow_resource(resource_name, fellow_name, quantity):
    if quantity <= 0:
        return "Quantity must be greater than zero."

    for resource in resources:

        if resource["name"].lower() == resource_name.lower():

            if resource["available"] < quantity:
                return "Not enough stock available."

            resource["available"] -= quantity
            resource["borrowed"] += quantity

            borrow_records.append({
                "fellow": fellow_name,
                "resource": resource["name"],
                "quantity": quantity
            })

            return "Borrowing successful."

    return "Resource not found."


def return_resource(resource_name, fellow_name, quantity):
    if quantity <= 0:
        return "Quantity must be greater than zero."

    for record in borrow_records:

        if (
            record["resource"].lower() == resource_name.lower()
            and record["fellow"].lower() == fellow_name.lower()
            and record["quantity"] >= quantity
        ):

            for resource in resources:

                if resource["name"].lower() == resource_name.lower():

                    resource["available"] += quantity
                    resource["borrowed"] -= quantity

                    record["quantity"] -= quantity

                    if record["quantity"] == 0:
                        borrow_records.remove(record)

                    return "Return successful."

            return "Resource not found."

    return "No matching borrowing record found."


def list_borrow_records():
    return borrow_records