"""
models.py - Contains class definitions for Product, Vendor, and PurchaseOrder.
"""

class Product:
    def __init__(self, product_id, name, category, quantity_in_stock, reorder_level, reorder_quantity, unit_price, vendor_id, active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity_in_stock = quantity_in_stock
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = active

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'category': self.category,
            'quantity_in_stock': self.quantity_in_stock,
            'reorder_level': self.reorder_level,
            'reorder_quantity': self.reorder_quantity,
            'unit_price': self.unit_price,
            'vendor_id': self.vendor_id,
            'active': self.active
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['product_id'],
            data['name'],
            data['category'],
            data['quantity_in_stock'],
            data['reorder_level'],
            data['reorder_quantity'],
            data['unit_price'],
            data['vendor_id'],
            data.get('active', True)
        )

    def display(self):
        status = "Active" if self.active else "Inactive"
        print(f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Stock: {self.quantity_in_stock}, Reorder Level: {self.reorder_level}, Price: ${self.unit_price:.2f}, Status: {status}")

    def is_low_stock(self):
        return self.quantity_in_stock <= self.reorder_level and self.active


class Vendor:
    def __init__(self, vendor_id, name, contact_name, phone, email, address):
        self.vendor_id = vendor_id
        self.name = name
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            'vendor_id': self.vendor_id,
            'name': self.name,
            'contact_name': self.contact_name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['vendor_id'],
            data['name'],
            data['contact_name'],
            data['phone'],
            data['email'],
            data['address']
        )

    def display(self):
        print(f"ID: {self.vendor_id}, Name: {self.name}, Contact: {self.contact_name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}")


class PurchaseOrder:
    def __init__(self, po_number, vendor_id, date_created, items, total_cost, status='Open'):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.date_created = date_created
        self.items = items  # list of dicts: {'product_id': str, 'quantity': int}
        self.total_cost = total_cost
        self.status = status  # 'Open', 'Received'

    def to_dict(self):
        return {
            'po_number': self.po_number,
            'vendor_id': self.vendor_id,
            'date_created': self.date_created,
            'items': self.items,
            'total_cost': self.total_cost,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['po_number'],
            data['vendor_id'],
            data['date_created'],
            data['items'],
            data['total_cost'],
            data.get('status', 'Open')
        )

    def display(self):
        print(f"PO: {self.po_number}, Vendor: {self.vendor_id}, Date: {self.date_created}, Total: ${self.total_cost:.2f}, Status: {self.status}")
        for item in self.items:
            print(f"  Product: {item['product_id']}, Quantity: {item['quantity']}")