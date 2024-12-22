schedule = (
                ("Monday", "Math", "English", "History"),
                ("Tuesday", "Biology", "Chemistry", "Physics")
            )

def display_schedule(schedule):
    for day_schedule in schedule:
        print(f"{day_schedule[0]}: {', '.join(day_schedule[1:])}")

def add_new_schedule(schedule, day, subjects):
    new_schedule = (day,) + tuple(subjects)
    return schedule + (new_schedule,)

def add_user_input_schedule(schedule, new_day, subjects):
    new_subjects = subjects.split(", ")
    schedule = add_new_schedule(schedule, new_day, new_subjects)
    return schedule

def main():
    print("Initial Schedule:")
    display_schedule(schedule)

    # Add new schedule
    new_day = input("Enter a day: ")
    subjects = input("Enter some subjects (separate by comma): ")

    user_input_new_schedule = add_user_input_schedule(schedule, new_day, subjects)

    print("\nUpdated Schedule:")
    display_schedule(user_input_new_schedule)

main()
