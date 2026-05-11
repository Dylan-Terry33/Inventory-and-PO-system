"""
file_manager.py - Contains functions for saving and loading data using JSON.
"""

import json
import os
from models import Product, Vendor, PurchaseOrder

DATA_FILE = 'inventory_data.json'

def save_data(products, vendors, purchase_orders):
    """
    Saves products, vendors, and purchase orders to a JSON file.
    Parameters: products (list of Product), vendors (list of Vendor), purchase_orders (list of PurchaseOrder)
    Returns: None
    """
    data = {
        'products': [p.to_dict() for p in products],
        'vendors': [v.to_dict() for v in vendors],
        'purchase_orders': [po.to_dict() for po in purchase_orders]
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully.")

def load_data():
    """
    Loads products, vendors, and purchase orders from a JSON file.
    Parameters: None
    Returns: tuple of (products list, vendors list, purchase_orders list)
    """
    if not os.path.exists(DATA_FILE):
        print("Data file not found. Starting with empty data.")
        return [], [], []
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        products = [Product.from_dict(p) for p in data.get('products', [])]
        vendors = [Vendor.from_dict(v) for v in data.get('vendors', [])]
        purchase_orders = [PurchaseOrder.from_dict(po) for po in data.get('purchase_orders', [])]
        print("Data loaded successfully.")
        return products, vendors, purchase_orders
    except json.JSONDecodeError:
        print("Error loading data. Starting with empty data.")
        return [], [], []

