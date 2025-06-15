# DO NOT MODIFY THE SECTIONS MARKED AS "DO NOT MODIFY"
# Sample inventory data - DO NOT MODIFY
product_ids = ["P001", "P002", "P003"]
names = ["Rice 5kg", "Wheat Flour 1kg", "Mobile Charger"]
categories = ["Grocery", "Grocery", "Electronics"]
quantities = [45, 8, 15]
prices = [250.00, 60.00, 300.00]

def find_low_stock_items(threshold):
    """
    Use a loop to find items with quantity below threshold
    Return lists of product details for low stock items
    """
    # Validation - DO NOT MODIFY
    if threshold is None: 
        raise TypeError("Threshold cannot be None")
    if not isinstance(threshold, int):
        raise TypeError("Threshold must be an integer")
    if threshold <= 0 or threshold > 100:
        raise ValueError("Threshold must be between 1 and 100")
        
    # Implementation using a for loop
    # 1. Create empty result lists (for ids, names, categories, quantities, prices)
    low_stock_ids = []
    low_stock_names = []
    low_stock_categories = []
    low_stock_quantities = []
    low_stock_prices = []
    
    # 2. Loop through the inventory using range(len(product_ids))
    for i in range(len(product_ids)):
        # 3. If an item's quantity is <= threshold, add its details to result lists
        if quantities[i] <= threshold:
            low_stock_ids.append(product_ids[i])
            low_stock_names.append(names[i])
            low_stock_categories.append(categories[i])
            low_stock_quantities.append(quantities[i])
            low_stock_prices.append(prices[i])
    
    # 4. Return the result lists
    return low_stock_ids, low_stock_names, low_stock_categories, low_stock_quantities, low_stock_prices

def search_products(term):
    """
    Use a loop to find items where name contains term (case-insensitive)
    Return lists of product details for matching items
    """
    # Validation - DO NOT MODIFY
    if term is None:
        raise TypeError("Search term cannot be None")
    if not isinstance(term, str):
        raise TypeError("Search term must be a string")
        
    # Implementation using a for loop
    # 1. Create empty result lists (for ids, names, categories, quantities, prices)
    matching_ids = []
    matching_names = []
    matching_categories = []
    matching_quantities = []
    matching_prices = []
    
    # 2. Convert search term to lowercase
    search_term = term.lower()
    
    # Handle empty search term case - return all items
    if not search_term:
        return product_ids[:], names[:], categories[:], quantities[:], prices[:]
    
    # 3. Loop through the inventory using range(len(names))
    for i in range(len(names)):
        # 4. If term is in item's name (case-insensitive), add to result lists
        if search_term in names[i].lower():
            matching_ids.append(product_ids[i])
            matching_names.append(names[i])
            matching_categories.append(categories[i])
            matching_quantities.append(quantities[i])
            matching_prices.append(prices[i])
    
    # 5. Return the result lists
    return matching_ids, matching_names, matching_categories, matching_quantities, matching_prices

def count_by_category():
    """
    Use nested loops to count items in each category
    Return lists of categories and their counts
    """
    # Implementation using nested loops
    # 1. Create a list for unique categories
    unique_categories = []
    
    # 2. Loop through categories to find unique ones
    for category in categories:
        if category not in unique_categories:
            unique_categories.append(category)
    
    # 3. Create a list for category counts
    category_counts = []
    
    # 4. For each unique category, loop through all categories to count occurrences
    for unique_cat in unique_categories:
        count = 0
        for i in range(len(categories)):
            if categories[i] == unique_cat:
                count += 1
        category_counts.append(count)
    
    # 5. Return both lists (unique categories and counts)
    return unique_categories, category_counts

def calculate_total_value():
    """
    Use a loop to calculate total value (quantity * price) of all items
    Return the total value as a float
    """
    # Implementation using a for loop
    # 1. Initialize total value as 0
    total_value = 0.0
    
    # 2. Loop through the inventory using range(len(quantities))
    for i in range(len(quantities)):
        # 3. Calculate item_value = quantities[i] * prices[i]
        item_value = quantities[i] * prices[i]
        # 4. Add item_value to total
        total_value += item_value
    
    # 5. Return the total value
    return total_value

def main():
    """
    Implement the main menu loop
    """
    # Implementation following skeleton TODO structure:
    print("\nWelcome to the Inventory Management System!")
    
    # 1. Create a loop to repeatedly show menu
    while True:
        print("\nInventory Management System - Main Menu")
        # 2. Show options (1-5)
        print("1. View Low Stock Items")
        print("2. Search Products")
        print("3. View Category Summary")
        print("4. Calculate Total Inventory Value")
        print("5. Exit")
        
        # 3. Get user choice
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # 4. Based on choice:
        if choice == '1':
            # For low stock items: Get threshold, call function, display results
            print("\n--- View Low Stock Items ---")
            try:
                threshold = int(input("Enter low stock threshold (1-100): "))
                low_ids, low_names, low_categories, low_quantities, low_prices = find_low_stock_items(threshold)
                
                print(f"\nLow Stock Items (threshold: {threshold}):")
                print("-" * 60)
                if len(low_ids) == 0:
                    print("No items below the specified threshold.")
                else:
                    print(f"{'ID':<8}{'Name':<20}{'Category':<12}{'Quantity':<10}{'Price':<10}")
                    print("-" * 60)
                    for i in range(len(low_ids)):
                        print(f"{low_ids[i]:<8}{low_names[i]:<20}{low_categories[i]:<12}{low_quantities[i]:<10}{low_prices[i]:<10.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            # For search: Get search term, call function, display results
            print("\n--- Search Products ---")
            try:
                search_term = input("Enter search term: ")
                search_ids, search_names, search_categories, search_quantities, search_prices = search_products(search_term)
                
                print(f"\nSearch Results for '{search_term}':")
                print("-" * 60)
                if len(search_ids) == 0:
                    print("No matching items found.")
                else:
                    print(f"{'ID':<8}{'Name':<20}{'Category':<12}{'Quantity':<10}{'Price':<10}")
                    print("-" * 60)
                    for i in range(len(search_ids)):
                        print(f"{search_ids[i]:<8}{search_names[i]:<20}{search_categories[i]:<12}{search_quantities[i]:<10}{search_prices[i]:<10.2f}")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            # For category count: Call function, display results
            print("\n--- Category Summary ---")
            try:
                unique_categories, category_counts = count_by_category()
                
                print("\nCategory Summary:")
                print("-" * 30)
                print(f"{'Category':<20}{'Count':<10}")
                print("-" * 30)
                for i in range(len(unique_categories)):
                    print(f"{unique_categories[i]:<20}{category_counts[i]:<10}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '4':
            # For total value: Call function, display result
            print("\n--- Total Inventory Value ---")
            try:
                total_value = calculate_total_value()
                print(f"\nTotal Inventory Value: ${total_value:,.2f}")
            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '5':
            # For exit: Break the loop
            print("Thank you for using the Inventory Management System!")
            break
            
        else:
            # 5. Handle invalid inputs
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()