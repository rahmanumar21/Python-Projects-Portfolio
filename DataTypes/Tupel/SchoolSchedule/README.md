# School Schedule Application

A simple Python program to display a school schedule based on the day of the week.

---

## Skills Demonstrated

### **Core Python Concepts:**
- **Tuples:** Store the weekly schedule as immutable sequences of subjects.
- **Loops:** Iterate over the schedule to find and display subjects for a given day.
- **Functions:** Modular design with `display_schedule()` to handle day-specific schedule display and `main()` for user interaction.
- **Input/Output:** Collect user input dynamically and display the corresponding schedule.
- **Conditionals:** Decision-making to handle user input validation and program flow.

---

## Example Output
```
=== School Schedule ===
Enter a day (e.g., Monday, Tuesday): Monday
Schedule for Monday:
Math
English
History

Do you want to try again? Type 'yes' or 'no': no
Thanks and Good Bye.
```

---

## How It Works

1. **Data Storage**:
   - The weekly schedule is stored in a tuple of tuples, where each sub-tuple contains the day of the week as the first element and subjects as the subsequent elements.

2. **Schedule Display**:
   - The `display_schedule()` function takes a day as input, searches the schedule, and displays the subjects for the matching day.
   - If the input day is invalid, the user is prompted with a message.

3. **User Interaction**:
   - The `main()` function provides an interactive loop that continuously allows users to input a day and view the corresponding schedule until they choose to exit.

4. **Case Insensitivity**:
   - The program ensures input is matched regardless of case by converting input and stored data to lowercase during comparisons.

5. **Dynamic Design**:
   - The schedule can easily be updated or extended by modifying the `schedule` tuple.

---

## About Me
**A. RAHMAN** - Python Developer & Tech Enthusiast

