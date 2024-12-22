# Location Finder System

A simple Python program to search for locations based on geographic coordinates (latitude and longitude).

---

## Skills Demonstrated

### **Core Python Concepts:**
- **Tuples:** Use tuples as immutable keys in the dictionary for coordinate pairs.
- **Dictionaries:** Store and manage a mapping between coordinates and location names.
- **Functions:** Modular design with `find_location()` for searching and `main()` for program interaction.
- **Input/Output:** Collect user input and display dynamic results.
- **Loops:** Facilitate continuous user interaction using a `while` loop.
- **Conditionals:** Decision-making to handle location searches and program termination.

---

## Example Output
```
=== Location Finder System ===
Enter latitude: 40.7128
Enter longitude: -74.0060
Location: New York, USA

Do you want to try again? type 'yes' or 'no': no
Thanks and Good bye.
```

---

## How It Works

1. **Data Storage**:
   - Locations are stored in a dictionary `locations` where keys are tuples of latitude and longitude, and values are location names.

2. **Search Functionality**:
   - The `find_location()` function checks if the given coordinates exist in the dictionary and returns the corresponding location name or "Location not found." if not found.

3. **User Interaction**:
   - The `main()` function provides an interactive loop where users can input latitude and longitude, view the result, and choose to continue or exit the application.

4. **Tuple Utilization**:
   - Tuples are utilized as dictionary keys due to their immutability, ensuring the integrity of coordinate-location mappings.

5. **Dynamic Design**:
   - The program is structured to allow easy expansion of the `locations` dictionary for more coordinate-location mappings.

---

## About Me
**A. RAHMAN** - Python Developer & Tech Enthusiast

