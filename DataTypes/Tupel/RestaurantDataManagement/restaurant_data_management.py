def display_menu(menu):
    print("\n=== Menu List ===")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i].title()}")

def add_menu(menu, new_menu_item):
    return menu + (new_menu_item,)

def promote_menu(menu):
    return menu * 2

def count_menu(menu, menu_name):
    return menu.count(menu_name)

def find_menu(menu, menu_name):
    if menu_name in menu:
        return menu.index(menu_name)
    else:
        return -1

# Initial restaurant menu
menu = ("fried rice", "chicken noodle", "chicken satay")

while True:

    print("\n===== Restaurant Menu Management Program =====")
    print("1. Display menu")
    print("2. Add new menu item")
    print("3. Duplicate menu for promotion")
    print("4. Count menu occurrences")
    print("5. Find menu index")
    print("6. Exit")

    choice = int(input("Choose an option (1-6): "))

    if choice == 1:
        display_menu(menu)
    elif choice == 2:
        new_menu_item = input("Enter a menu here: ")
        menu = add_menu(menu, new_menu_item)
        print("\nMenu item added successfully!")
        display_menu(menu)
    elif choice == 3:
        promoted = promote_menu(menu)
        print("\nnPromotional Menu:")
        print(', '.join(promoted).title())
    elif choice == 4:
        menu_to_count = input("Which menu item would you like to count? ")
        result = count_menu(menu, menu_to_count)
        print(f'The menu item "{menu_to_count}" appears {result} times.')
    elif choice == 5:
        menu_to_find = input("Which menu item would you like to find? ")
        result = find_menu(menu, menu_to_find)

        if result != -1:
            print(f'The menu item {menu_to_find.title()} is found at index {result}.')
        else:
            print(f'The menu item {menu_to_find.title()} is not found.')



