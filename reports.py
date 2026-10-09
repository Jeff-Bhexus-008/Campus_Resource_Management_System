from inventory import resources


def generate_report():
    total_resources = 0
    total_available = 0
    total_borrowed = 0

    for resource in resources:
        total_resources += resource["total"]
        total_available += resource["available"]
        total_borrowed += resource["borrowed"]

    return {
        "total": total_resources,
        "available": total_available,
        "borrowed": total_borrowed
    }


def low_stock_resources(threshold=1):
    results = []

    for resource in resources:
        if resource["available"] <= threshold:
            results.append(resource)

    return results


def most_borrowed_resource():
    if not resources:
        return None

    most_borrowed = resources[0]

    for resource in resources:
        if resource["borrowed"] > most_borrowed["borrowed"]:
            most_borrowed = resource

    return most_borrowed