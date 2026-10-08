def find_record(records, fellow_id, resource_id):
    for record in records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:
            return record
    return None


def borrow_resource(resources, fellows, records):
    fellow_id = input("Fellow ID: ").upper()

    if fellow_id not in fellows:
        print("Fellow ID does not exist.")
        return

    resource_id = input("Resource ID: ").upper()

    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item

    if resource is None:
        print("Resource ID does not exist.")
        return

    try:
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Enter a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if quantity > resource["available"]:
        print("Not enough stock.")
        return

    resource["available"] -= quantity

    record = find_record(records, fellow_id, resource_id)

    if record:
        record["quantity"] += quantity
    else:
        records.append({
            "fellow_id": fellow_id,
            "resource_id": resource_id,
            "quantity": quantity
        })

    print("Borrowing successful.")


def return_resource(resources, fellows, records):
    fellow_id = input("Fellow ID: ").upper()

    if fellow_id not in fellows:
        print("Fellow ID does not exist.")
        return

    resource_id = input("Resource ID: ").upper()

    record = find_record(records, fellow_id, resource_id)

    if record is None:
        print("This fellow does not have this resource.")
        return

    try:
        quantity = int(input("Quantity to return: "))
    except ValueError:
        print("Enter a whole number.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if quantity > record["quantity"]:
        print("The fellow does not have that many on loan.")
        return

    for resource in resources:
        if resource["id"] == resource_id:
            resource["available"] += quantity

    record["quantity"] -= quantity

    if record["quantity"] == 0:
        records.remove(record)

    print("Return successful.")