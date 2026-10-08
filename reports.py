def report(resources):
    total = 0
    available = 0

    for resource in resources:
        total += resource["total"]
        available += resource["available"]

    borrowed = total - available

    print("\n--- REPORT ---")
    print("Total units:", total)
    print("Available units:", available)
    print("Borrowed units:", borrowed)

    print("\nLow stock:")

    for resource in resources:
        if resource["available"] < 3:
            print(resource["name"], "-", resource["available"])

    highest = 0

    for resource in resources:
        borrowed_units = resource["total"] - resource["available"]

        if borrowed_units > highest:
            highest = borrowed_units

    print("\nMost borrowed:")

    for resource in resources:
        borrowed_units = resource["total"] - resource["available"]

        if borrowed_units == highest and highest > 0:
            print(resource["name"], "-", borrowed_units)