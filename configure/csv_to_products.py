import csv
import json

# Define the columns to keep (product-related fields)
PRODUCT_FIELDS = [
    "product_id", "product_title", "product_attr", "product_link", "product_image",
    "product_amount", "product_price", "Voltage/Power", "Material", "Dimensions",
    "Certifications", "Key_Specs"
]

# Read the CSV and write the filtered JSON
with open("order_list.csv", "r", encoding="utf-8") as csvfile:
    # Detect delimiter from first line
    first_line = csvfile.readline()
    delimiter = "|" if "|" in first_line else ","
    # Read header
    header_line = csvfile.readline().lstrip("# ").strip()
    reader = csv.DictReader(csvfile, fieldnames=header_line.split(delimiter), delimiter=delimiter)
    products = []
    for row in reader:
        product = {field: row.get(field, "") for field in PRODUCT_FIELDS}
        # Only add if product_id and product_title are present
        if product["product_id"] and product["product_title"]:
            products.append(product)

with open("products.json", "w", encoding="utf-8") as jsonfile:
    json.dump(products, jsonfile, ensure_ascii=False, indent=2)
