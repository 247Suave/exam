import json


class PlaceToStay:
    def __init__(self, name, type, address, availability):
        self.name = name
        self.type = type
        self.address = address
        self.availability = availability

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.address}, Availability: {self.availability}"


def add_place_to_stay():
    name = input("Enter the name of the place: ")
    type = input("Enter the type of the place: ")
    address = input("Enter the address of the place: ")
    availability = int(input("Enter the availability of the place: "))

    # Handle input validation for availability
    while True:
        availability_input = input("Enter the availability of the place: ")
        try:
            availability = int(availability_input)
            if availability >= 0:  # Ensure availability is a non-negative integer
                break
            else:
                print("Availability must be a non-negative integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for availability.")

    place = PlaceToStay(name, type, address, availability)
    places.append(place)


def search_place_by_name():
    search_name = input("Enter the name to search for: ")
    found_places = [place for place in places if search_name.lower() in place.name.lower()]

    if found_places:
        for place in found_places:
            print(place)
    else:
        print(f"No places found with the name '{search_name}'.")


def display_all_places_sorted_by_name():
    if places:
        sorted_places = sorted(places, key=lambda x: x.name.lower())
        for place in sorted_places:
            print(place)
    else:
        print("No places to display.")


def search_place_by_type():
    search_type = input("Enter the type to search for: ")
    found_places = [place for place in places if search_type.lower() in place.type.lower()]

    if found_places:
        for place in found_places:
            print(place)
    else:
        print(f"No places found with the type '{search_type}'.")


def make_booking():
    search_name = input("Enter the name of the place to book: ")
    found_place = next((place for place in places if search_name.lower() in place.name.lower()), None)

    if found_place:
        if found_place.availability > 0:
            found_place.availability -= 1
            print(f"Booking successful for {found_place.name}. Availability reduced to {found_place.availability}.")
        else:
            print(f"Sorry, {found_place.name} is fully booked.")
    else:
        print(f"No places found with the name '{search_name}'.")


def save_and_load_to_file():
    with open('places.json', 'w') as file:
        json.dump([place.__dict__ for place in places], file)

    try:
        with open('places.json', 'r') as file:
            loaded_places = json.load(file)
            places.clear()
            places.extend([PlaceToStay(**place) for place in loaded_places])
    except FileNotFoundError:
        print("No file found for loading.")


# Sample data
places = [
    PlaceToStay("Hotel A", "Hotel", "123 Main St", 10),
    PlaceToStay("Hostel B", "Hostel", "456 Side St", 5),
    # Add more sample data as needed
]

while True:
    print("\nMenu:")
    print("1. Add a new place to stay")
    print("2. Search for a specific place to stay")
    print("3. Display all places to stay sorted by name")
    print("4. Search for a place to stay by type")
    print("5. Make a booking")
    print("6. Save and load places to/from file")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_place_to_stay()
    elif choice == '2':
        search_place_by_name()
    elif choice == '3':
        display_all_places_sorted_by_name()
    elif choice == '4':
        search_place_by_type()
    elif choice == '5':
        make_booking()
    elif choice == '6':
        save_and_load_to_file()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")
