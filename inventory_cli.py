def edit_product_field(product):
    keys = list(product.keys())
    for fidx, key in enumerate(keys, 1):
        print(f"{fidx}: {key.capitalize()} (current: {product[key]})")
    field_num = input("Enter field number to edit (or press Enter to cancel): ").strip()
    if field_num.isdigit() and 1 <= int(field_num) <= len(keys):
        field = keys[int(field_num)-1]
        current = product[field]
        new_val = input(f"Enter new value for {field} (current: {current}): ").strip()
        if new_val:
            product[field] = new_val
            print(f"{field.capitalize()} updated to: {new_val}")
            return True
        else:
            print("No change made.")
    else:
        print("Cancelled or invalid selection.")
    return False

import json
import sys

PRODUCTS_FILE = 'products.json'

def load_products():
    with open(PRODUCTS_FILE, 'r') as f:
        return json.load(f)

"""
        choice = input("Enter your choice: ").strip()
        action = actions.get(choice)
        if action:
            action(products)
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
