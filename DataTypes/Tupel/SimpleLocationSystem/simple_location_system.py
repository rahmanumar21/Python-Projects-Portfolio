# Location data stored as tuples (latitude, longitude)
locations = {
    (40.7128, -74.0060): "New York, USA",
    (34.0522, -118.2437): "Los Angeles, USA",
    (48.8566, 2.3522): "Paris, France",
    (35.6895, 139.6917): "Tokyo, Japan",
    (-33.8688, 151.2093): "Sydney, Australia"
}

def find_location(latitude, longitude):
    coordinates = (latitude, longitude)

    if coordinates in locations:
        return f"Location: {locations[coordinates]}"
    else:
        return "Location not found."

def main():

    while True:
        print("=== Location Finder System ===")
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))

        result = find_location(latitude, longitude)
        print(result)

        close_app = input("Do you want to try again? type 'yes' or 'no': ")
        if close_app != "yes":
            print("Thanks and Good bye.")
            break

main()
