# Main app menus
main_app_menus = ("Display Product Categories", "Display Stock by Category",
                  "Add a New Category", "Add Stock to a Category",
                  "Remove Out-of-Stock Item", "Exit")

# Categories and stock items
categories = {
    "Food and Beverages",
    "Health and Beauty",
    "Clothing and Accessories",
    "Electronics and Gadgets",
    "Household Supplies",
    "Automotive",
    "Baby and Kids' Products"
}

stock_items = {
    "Food and Beverages": {
        "Rice (10 kg)", "Mineral Water (20 bottles)", "Chocolate Bars (50 pieces)", "Frozen Pizza (5 packs)"
    },
    "Health and Beauty": {
        "Shampoo (20 bottles)", "Face Wash (15 tubes)", "Multivitamins (30 packs)",
        "Pain Relief Cream (10 tubes)"
    },
    "Clothing and Accessories": {
        "Men's T-Shirts (10 units)", "Women's Dresses (8 units)", "Kids' Shoes (5 pairs)", "Handbags (3 units)"
    },
    "Electronics and Gadgets": {
        "Smartphones (2 units)", "Earphones (5 pairs)", "Laptops (1 unit)", "USB Drives (10 units)"
    },
    "Household Supplies": {
        "Cooking Pans (5 units)", "Cleaning Mops (10 units)", "Curtains (4 sets)",
        "Laundry Detergent (15 packs)"
    },
    "Automotive": {
        "Motor Oil (5 liters)", "Car Seat Covers (3 sets)", "Vehicle Air Fresheners (10 units)"
    },
    "Baby and Kids' Products": {
        "Baby Diapers (20 packs)", "Milk Formula (10 cans)", "Kids' Toys (5 items)", "Baby Wipes (15 packs)"
    }
}

def display_main_app_menus(main_app_menus):
    print("\n===== Online Store Management System =====")
    for i, menu in enumerate(main_app_menus, start=1):
        print(f'{i}. {menu}')

def display_categories(categories):
    print("\n=== Product Categories ===")
    for i, category in enumerate(categories, start=1):
        print(f'{i}. {category}')

def add_category(categories):
    new_category = input("Enter a new category: ").strip()
    if new_category in categories:
        print(f'Category "{new_category}" already exists!')
    else:
        categories.add(new_category)
        print(f'Category "{new_category}" added successfully!')

def display_stock_by_category(stock_items):
    category = input("Enter the category to view stock: ").strip()
    if category in stock_items:
        print(f'\n==== Stock "{category}" ====')
        for item in stock_items[category]:
            print(f'- {item}')
    else:
        print("Category not found.")

def add_stock(stock_items):
    category = input("Enter the category to add stock: ").strip()
    if category in stock_items:
        new_stock = input("Enter the new stock item: ").strip()
        if new_stock in stock_items[category]:
            print(f'Stock item "{new_stock}" already exists in "{category}".')
        else:
            stock_items[category].add(new_stock)
            print(f'Stock item "{new_stock}" added to "{category}".')
    else:
        print("Category not found.")

def remove_out_of_stock(stock_items):
    category = input("Enter the category: ").strip()
    if category in stock_items:
        item = input("Enter the out-of-stock item: ").strip()
        if item not in stock_items[category]:
            print(f'Item "{item}" not found in "{category}".')
        else:
            stock_items[category].remove(item)
            print(f'Item "{item}" successfully removed from "{category}".')
    else:
        print("Category not found!")

def main():
    while True:
        display_main_app_menus(main_app_menus)
        count_menus = len(main_app_menus)
        choice = int(input(f"Choose an option (1–{count_menus}): "))

        if choice == 1:
            display_categories(categories)
        elif choice == 2:
            display_stock_by_category(stock_items)
        elif choice == 3:
            add_category(categories)
        elif choice == 4:
            add_stock(stock_items)
        elif choice == 5:
            remove_out_of_stock(stock_items)
        elif choice == 6:
            print("Program terminated. Thank you!")
            break
        else:
            print(f"Invalid option! Please choose between 1 and {count_menus}.")

main()


