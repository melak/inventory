import json
from .product_model import Product

PRODUCTS_FILE = 'products.json'

class ProductRepository:
    def __init__(self, file_path=PRODUCTS_FILE):
        self.file_path = file_path

    def load_products(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return [Product(p) for p in data if not (p.get('deleted') is True or p.get('deleted') == 'True')]

    def save_products(self, products):
        with open(self.file_path, 'w') as f:
            json.dump([p.data for p in products], f, indent=2)

    def create_empty_product(self, title):
        # Minimal required fields for a new product
        from .product_model import Product
        product_data = {
            'product_id': '',
            'product_title': title,
            'product_attr': '',
            'product_link': '',
            'product_image': '',
            'product_amount': '',
            'product_price': '',
            'Voltage/Power': '',
            'Material': '',
            'Dimensions': '',
            'Certifications': '',
            'Key_Specs': '',
            'location': ''
        }
        return Product(product_data)
