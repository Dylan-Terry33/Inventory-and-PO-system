"""
reports.py - Contains all reporting functions.
"""

from models import Product, Vendor, PurchaseOrder

def full_inventory_report(products):
    """
    Generates full inventory report.
    Parameters: products (list)
    Returns: None
    """
    print("Full Inventory Report:")
    for p in products:
        if p.active:
            p.display()

def low_stock_report(products):
    """
    Generates low-stock report.
    Parameters: products (list)
    Returns: None
    """
    print("Low-Stock Report:")
    low_stock = [p for p in products if p.is_low_stock()]
    for p in low_stock:
        p.display()

def total_inventory_value_report(products):
    """
    Calculates and displays total inventory value.
    Parameters: products (list)
    Returns: None
    """
    total_value = sum(p.quantity_in_stock * p.unit_price for p in products if p.active)
    print(f"Total Inventory Value: ${total_value:.2f}")

def open_purchase_orders_report(purchase_orders):
    """
    Displays open purchase orders.
    Parameters: purchase_orders (list)
    Returns: None
    """
    print("Open Purchase Orders:")
    for po in purchase_orders:
        if po.status == 'Open':
            po.display()

def received_purchase_orders_report(purchase_orders):
    """
    Displays received purchase orders.
    Parameters: purchase_orders (list)
    Returns: None
    """
    print("Received Purchase Orders:")
    for po in purchase_orders:
        if po.status == 'Received':
            po.display()

def vendor_report(vendors, products):
    """
    Reports products by vendor.
    Parameters: vendors (list), products (list)
    Returns: None
    """
    print("Vendor Report:")
    for v in vendors:
        print(f"\nVendor: {v.name}")
        vendor_products = [p for p in products if p.vendor_id == v.vendor_id and p.active]
        for p in vendor_products:
            p.display()

def export_report_to_text(products, filename="inventory_report.txt"):
    """
    Exports full inventory report to a text file (unique feature).
    Parameters: products (list), filename (str)
    Returns: None
    """
    with open(filename, 'w') as f:
        f.write("Full Inventory Report\n")
        for p in products:
            if p.active:
                f.write(f"ID: {p.product_id}, Name: {p.name}, Stock: {p.quantity_in_stock}, Price: ${p.unit_price:.2f}\n")
    print(f"Report exported to {filename}.")