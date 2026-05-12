"""
inventory_manager.py - Contains core functions for managing inventory and purchase orders.
"""

from models import Product, Vendor, PurchaseOrder
from datetime import datetime

def add_product(products, vendors):
    """
    Adds a new product after validating input.
    Parameters: products (list), vendors (list)
    Returns: None
    """
    try:
        product_id = input("Enter product ID: ").strip()
        if any(p.product_id == product_id for p in products):
            print("Product ID already exists.")
            return
        name = input("Enter product name: ").strip()
        category = input("Enter category: ").strip()
        quantity_in_stock = int(input("Enter quantity in stock: "))
        reorder_level = int(input("Enter reorder level: "))
        reorder_quantity = int(input("Enter reorder quantity: "))
        unit_price = float(input("Enter unit price: "))
        vendor_id = input("Enter vendor ID: ").strip()
        if not any(v.vendor_id == vendor_id for v in vendors):
            print("Vendor ID does not exist.")
            return
        product = Product(product_id, name, category, quantity_in_stock, reorder_level, reorder_quantity, unit_price, vendor_id)
        products.append(product)
        print("Product added.")
    except ValueError:
        print("Invalid input. Please enter numbers where required.")

def view_products(products):
    """
    Displays all active products.
    Parameters: products (list)
    Returns: None
    """
    for p in products:
        if p.active:
            p.display()

def search_products(products, query):
    """
    Searches products by ID, name, or category.
    Parameters: products (list), query (str)
    Returns: list of matching products
    """
    results = []
    for p in products:
        if query.lower() in p.product_id.lower() or query.lower() in p.name.lower() or query.lower() in p.category.lower():
            results.append(p)
    return results

def edit_product(products, vendors):
    """
    Edits an existing product.
    Parameters: products (list), vendors (list)
    Returns: None
    """
    product_id = input("Enter product ID to edit: ").strip()
    product = next((p for p in products if p.product_id == product_id), None)
    if not product:
        print("Product not found.")
        return
    # Similar to add, but update fields
    try:
        product.name = input(f"Name ({product.name}): ").strip() or product.name
        product.category = input(f"Category ({product.category}): ").strip() or product.category
        product.quantity_in_stock = int(input(f"Quantity ({product.quantity_in_stock}): ") or product.quantity_in_stock)
        product.reorder_level = int(input(f"Reorder level ({product.reorder_level}): ") or product.reorder_level)
        product.reorder_quantity = int(input(f"Reorder quantity ({product.reorder_quantity}): ") or product.reorder_quantity)
        product.unit_price = float(input(f"Unit price ({product.unit_price}): ") or product.unit_price)
        vendor_id = input(f"Vendor ID ({product.vendor_id}): ").strip() or product.vendor_id
        if not any(v.vendor_id == vendor_id for v in vendors):
            print("Vendor ID does not exist.")
            return
        product.vendor_id = vendor_id
        print("Product updated.")
    except ValueError:
        print("Invalid input.")

def deactivate_product(products):
    """
    Deactivates a product.
    Parameters: products (list)
    Returns: None
    """
    product_id = input("Enter product ID to deactivate: ").strip()
    product = next((p for p in products if p.product_id == product_id), None)
    if not product:
        print("Product not found.")
        return
    product.active = False
    print("Product deactivated.")

def display_low_stock(products):
    """
    Displays low-stock products.
    Parameters: products (list)
    Returns: None
    """
    low_stock = [p for p in products if p.is_low_stock()]
    for p in low_stock:
        p.display()

def add_vendor(vendors):
    """
    Adds a new vendor.
    Parameters: vendors (list)
    Returns: None
    """
    vendor_id = input("Enter vendor ID: ").strip()
    if any(v.vendor_id == vendor_id for v in vendors):
        print("Vendor ID already exists.")
        return
    name = input("Enter vendor name: ").strip()
    contact_name = input("Enter contact name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    vendor = Vendor(vendor_id, name, contact_name, phone, email, address)
    vendors.append(vendor)
    print("Vendor added.")

def view_vendors(vendors):
    """
    Displays all vendors.
    Parameters: vendors (list)
    Returns: None
    """
    for v in vendors:
        v.display()

def search_vendors(vendors, query):
    """
    Searches vendors by ID or name.
    Parameters: vendors (list), query (str)
    Returns: list of matching vendors
    """
    results = []
    for v in vendors:
        if query.lower() in v.vendor_id.lower() or query.lower() in v.name.lower():
            results.append(v)
    return results

def edit_vendor(vendors):
    """
    Edits a vendor.
    Parameters: vendors (list)
    Returns: None
    """
    vendor_id = input("Enter vendor ID to edit: ").strip()
    vendor = next((v for v in vendors if v.vendor_id == vendor_id), None)
    if not vendor:
        print("Vendor not found.")
        return
    vendor.name = input(f"Name ({vendor.name}): ").strip() or vendor.name
    vendor.contact_name = input(f"Contact ({vendor.contact_name}): ").strip() or vendor.contact_name
    vendor.phone = input(f"Phone ({vendor.phone}): ").strip() or vendor.phone
    vendor.email = input(f"Email ({vendor.email}): ").strip() or vendor.email
    vendor.address = input(f"Address ({vendor.address}): ").strip() or vendor.address
    print("Vendor updated.")

def create_purchase_order(products, vendors, purchase_orders):
    """
    Creates a new purchase order.
    Parameters: products (list), vendors (list), purchase_orders (list)
    Returns: None
    """
    po_number = input("Enter PO number: ").strip()
    if any(po.po_number == po_number for po in purchase_orders):
        print("PO number already exists.")
        return
    vendor_id = input("Enter vendor ID: ").strip()
    if not any(v.vendor_id == vendor_id for v in vendors):
        print("Vendor not found.")
        return
    date_created = datetime.now().strftime("%Y-%m-%d")
    items = []
    total_cost = 0
    while True:
        product_id = input("Enter product ID (or 'done'): ").strip()
        if product_id.lower() == 'done':
            break
        product = next((p for p in products if p.product_id == product_id), None)
        if not product:
            print("Product not found.")
            continue
        try:
            quantity = int(input("Enter quantity: "))
            items.append({'product_id': product_id, 'quantity': quantity})
            total_cost += quantity * product.unit_price
        except ValueError:
            print("Invalid quantity.")
    if not items:
        print("No items added.")
        return
    po = PurchaseOrder(po_number, vendor_id, date_created, items, total_cost)
    purchase_orders.append(po)
    print("Purchase order created.")

def view_purchase_orders(purchase_orders):
    """
    Displays all purchase orders.
    Parameters: purchase_orders (list)
    Returns: None
    """
    for po in purchase_orders:
        po.display()

def receive_shipment(products, purchase_orders):
    """
    Marks a PO as received and updates inventory.
    Parameters: products (list), purchase_orders (list)
    Returns: None
    """
    po_number = input("Enter PO number to receive: ").strip()
    po = next((po for po in purchase_orders if po.po_number == po_number), None)
    if not po:
        print("PO not found.")
        return
    if po.status == 'Received':
        print("PO already received.")
        return
    for item in po.items:
        product = next((p for p in products if p.product_id == item['product_id']), None)
        if product:
            product.quantity_in_stock += item['quantity']
    po.status = 'Received'
    print("Shipment received and inventory updated.")

def sort_products_by_name(products):
    """
    Sorts products by name.
    Parameters: products (list)
    Returns: sorted list
    """
    return sorted(products, key=lambda p: p.name)

def sort_products_by_quantity(products):
    """
    Sorts products by quantity in stock.
    Parameters: products (list)
    Returns: sorted list
    """
    return sorted(products, key=lambda p: p.quantity_in_stock)

def sort_products_by_price(products):
    """
    Sorts products by unit price.
    Parameters: products (list)
    Returns: sorted list
    """
    return sorted(products, key=lambda p: p.unit_price)

def sort_purchase_orders_by_date(purchase_orders):
    """
    Sorts POs by date.
    Parameters: purchase_orders (list)
    Returns: sorted list
    """
    return sorted(purchase_orders, key=lambda po: po.date_created)