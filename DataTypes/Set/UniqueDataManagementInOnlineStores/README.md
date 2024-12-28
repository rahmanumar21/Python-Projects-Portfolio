# Online Store Management System

A Python application for managing product categories and stock items in an online store. This project demonstrates the use of **sets** combined with lists and dictionaries for efficient data management, while emphasizing the core functionality of sets.

---

## Skills Demonstrated

### **Core Python Concepts:**
- **Sets:** Efficiently store and manage unique product categories and stock items.
- **Dictionaries:** Organize stock items by category for quick access.
- **Lists:** Display ordered menus and categories.
- **Functions:** Modular design for each functionality such as displaying categories, adding stock, and removing items.
- **Input/Output:** Collect and display data dynamically through the console.
- **Error Handling:** Validate user inputs to ensure smooth interaction.

---

## Example Output
```
===== Online Store Management System =====
1. Display Product Categories
2. Display Stock by Category
3. Add a New Category
4. Add Stock to a Category
5. Remove Out-of-Stock Item
6. Exit

Choose an option (1–6): 1

=== Product Categories ===
1. Food and Beverages
2. Health and Beauty
3. Clothing and Accessories
4. Electronics and Gadgets
5. Household Supplies
6. Automotive
7. Baby and Kids' Products

Choose an option (1–6): 4
Enter the category to add stock: Electronics and Gadgets
Enter the new stock item: Smartwatch (3 units)
Stock item "Smartwatch (3 units)" added to "Electronics and Gadgets".
```

---

## How It Works

1. **Main Menu**:
   - The `main_app_menus` tuple contains a list of main menu options for user interaction.
   - The `display_main_app_menus()` function displays the menu to the user.

2. **Product Categories**:
   - Categories are stored in a set `categories` to ensure each category is unique.
   - The `display_categories()` function lists all available categories.
   - The `add_category()` function allows users to add a new category, preventing duplicates.

3. **Stock Management**:
   - Stock items are stored in a dictionary `stock_items`, where keys are categories (from the `categories` set) and values are sets of stock items.
   - The `display_stock_by_category()` function displays stock items for a chosen category.
   - The `add_stock()` function adds a new stock item to a category, ensuring no duplicates within the category.
   - The `remove_out_of_stock()` function removes an item from a category when it is no longer in stock.

4. **Interactive Workflow**:
   - Users interact with the system through a loop in the `main()` function, choosing operations until they decide to exit.

5. **Emphasis on Sets**:
   - Sets are used for both categories and stock items to prevent duplicates and ensure efficient membership testing.

---

## About Me
**A. RAHMAN** - Python Developer & Tech Enthusiast

