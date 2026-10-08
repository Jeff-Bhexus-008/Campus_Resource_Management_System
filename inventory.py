def find_resource(resources, resource_id):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    return None


def add_resource(resources):
    resource_id = input("Resource ID: ").upper()

    if find_resource(resources, resource_id):
        print("That ID already exists.")
        return

    name = input("Resource name: ")
    category = input("Category: ")

    try:
        total = int(input("Total units: "))
    except ValueError:
        print("Enter a whole number.")
        return

    if total <= 0:
        print("Units must be greater than 0.")
        return

    resources.append({
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    })

    print("Resource added.")


def list_resources(resources):
    for resource in resources:
        print(
            resource["id"],
            resource["name"],
            resource["category"],
            "Total:", resource["total"],
            "Available:", resource["available"]
        )


def search_resources(resources):
    name = input("Search name: ").lower()

    for resource in resources:
        if name in resource["name"].lower():
            print(resource)


def filter_category(resources):
    category = input("Category: ").lower()

    for resource in resources:
        if resource["category"].lower() == category:
            print(resource)