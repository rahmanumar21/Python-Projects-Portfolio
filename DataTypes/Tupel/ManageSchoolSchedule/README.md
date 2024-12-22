# Dynamic School Schedule Application

A Python application for managing and dynamically updating a school schedule. Users can view the current schedule and add new days and subjects interactively.

---

## Skills Demonstrated

### **Core Python Concepts:**
- **Tuples:** Use tuples for immutable schedule storage and manipulation.
- **Functions:** Modular design with reusable functions like `display_schedule()` and `add_new_schedule()`.
- **String Manipulation:** Format and split user inputs to create new schedule entries.
- **Input/Output:** Dynamically collect and display data through the console.
- **Data Updates:** Append new schedule data without altering the original immutable structure.

---

## Example Output
```
Initial Schedule:
Monday: Math, English, History
Tuesday: Biology, Chemistry, Physics

Enter a day: Wednesday
Enter some subjects (separate by comma): Art, Physical Education

Updated Schedule:
Monday: Math, English, History
Tuesday: Biology, Chemistry, Physics
Wednesday: Art, Physical Education
```

---

## How It Works

1. **Data Storage**:
   - The schedule is stored as a tuple of tuples, where each sub-tuple contains a day and its corresponding subjects.

2. **Schedule Display**:
   - The `display_schedule()` function prints the current schedule, showing each day with its subjects.

3. **Add New Schedule**:
   - The `add_new_schedule()` function takes a day and a list of subjects as input, creates a new tuple, and appends it to the existing schedule.
   - The `add_user_input_schedule()` function collects user input for a new day and subjects, processes the input, and updates the schedule.

4. **User Interaction**:
   - The `main()` function displays the initial schedule, prompts the user to add a new schedule, and then displays the updated schedule.

5. **Dynamic Updates**:
   - The immutable tuple structure ensures the original schedule remains unaltered while the updated schedule is created as a new object.

---

## About Me
**A. RAHMAN** - Python Developer & Tech Enthusiast

