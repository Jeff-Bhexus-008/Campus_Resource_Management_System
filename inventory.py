resources = [
    {
        "name": "Laptop",
        "category": "Electronics",
        "total": 5,
        "available": 4,
        "borrowed": 1
    },
    {
        "name": "Mouse",
        "category": "Accessories",
        "total": 4,
        "available": 4,
        "borrowed": 0
    },
    {
        "name": "Keyboard",
        "category": "Accessories",
        "total": 3,
        "available": 1,
        "borrowed": 2
    },
    {
        "name": "Projector",
        "category": "Electronics",
        "total": 2,
        "available": 2,
        "borrowed": 0
    },
    {
        "name": "Monitor",
        "category": "Electronics",
        "total": 4,
        "available": 3,
        "borrowed": 1
    }
]


def add_resource(name, category, quantity):
    if quantity <= 0:
        return "Quantity must be greater than zero."

    for resource in resources:
        if resource["name"].lower() == name.lower():
            resource["total"] += quantity
            resource["available"] += quantity
            return "Resource quantity updated successfully."

    resources.append({
        "name": name,
        "category": category,
        "total": quantity,
        "available": quantity,
        "borrowed": 0
    })

    return "Resource added successfully."


def list_resources():
    return resources


def search_resources(keyword):
    results = []

    keyword = keyword.lower()

    for resource in resources:
        if keyword in resource["name"].lower():
            results.append(resource)

    return results


def filter_category(category):
    results = []

    category = category.lower()

    for resource in resources:
        if resource["category"].lower() == category:
            results.append(resource)

    return results