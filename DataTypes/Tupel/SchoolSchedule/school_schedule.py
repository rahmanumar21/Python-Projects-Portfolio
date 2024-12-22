# School schedule stored as tuples
schedule = (
    ("Monday", "Math", "English", "History"),
    ("Tuesday", "Biology", "Chemistry", "Physics"),
    ("Wednesday", "Math", "Physical Education", "Art"),
    ("Thursday", "English", "Geography", "History"),
    ("Friday", "Math", "Computer Science", "Physics")
)

def display_schedule(day):
    for daily_schedule in schedule:
        if daily_schedule[0].lower() == day.lower():
            print(f"Schedule for {daily_schedule[0]}:")
            for subject in daily_schedule[1:]:
                print(subject)
            return
    print("Data not found. Please enter a valid day.")


def main():
    print("=== School Schedule ===")
    day = input("Enter a day (e.g., Monday, Tuesday): ")
    display_schedule(day)

while True:
    main()
    close_app = input("Do you want to try again? Type 'yes' or 'no': ")
    if close_app != "yes":
        print("Thanks and Good Bye.")
        break
