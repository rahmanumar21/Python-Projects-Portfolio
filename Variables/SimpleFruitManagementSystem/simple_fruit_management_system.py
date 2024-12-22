import art

fruits = ["Apple", "Banana", "Cherry", "Date"]

def add_fruits_from_input(user_input):
    fruit1, fruit2, fruit3 = user_input.split(",")
    fruit1, fruit2, fruit3 = fruit1.strip(), fruit2.strip(), fruit3.strip()
    fruits.extend([fruit1, fruit2, fruit3])

def main():

    while True:
        print(art.fruit_shop)

        user_input = input("Enter three new fruits separated by commas: ").title()
        add_fruits_from_input(user_input)

        print("Current list of fruits:")
        for i, fruit in enumerate(fruits, start=1):
            print(f"{i}. {fruit}")

        first_fruit, second_fruit, *remaining_fruit = fruits

        print("Unpacking the list of fruits:")
        print(f"First fruit: {first_fruit}")
        print(f"Second fruit: {second_fruit}")
        print(f"Remaining fruit: {remaining_fruit}")

        close_app = input("Do you want to add more? type 'yes' or 'no': ")
        if close_app != "yes":
            print("Thanks and Good bye.")
            break

main()