# Picnic Calculator: Calculates the total items brought by the guests.

guests = {
    "Ali": {
        "Sandwiches": 4,
        "Juices": 2,
        "Apples": 5
    },
    "Sara": {
        "Sandwiches": 3,
        "Juices": 4,
        "Apples": 2
    },
    "Ahmed": {
        "Sandwiches": 5,
        "Juices": 1,
        "Apples": 6
    }
}

total_sandwiches = 0
total_juices = 0
total_apples = 0

for guest in guests:
    total_sandwiches += guests[guest]["Sandwiches"]
    total_juices += guests[guest]["Juices"]
    total_apples += guests[guest]["Apples"]


print("=== Picnic Items ===")
print(f"Total Sandwiches: {total_sandwiches}")
print(f"Total Juices: {total_juices}")
print(f"Total Apples: {total_apples}")