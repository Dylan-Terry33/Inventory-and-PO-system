"""
main.py - Contains the main menu and starts the program.
"""

from inventory_manager import *
from file_manager import save_data, load_data
from reports import *
import sys

def main_menu(products, vendors, purchase_orders):
    """
    Displays the main menu and handles user choices.
    Parameters: products (list), vendors (list), purchase_orders (list)
    Returns: None
    """
    while True:
        print("\nMain Menu:")
        print("1. Product Management")
        print("2. Vendor Management")
        print("3. Purchase Orders")
        print("4. Reports")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            product_menu(products, vendors)
        elif choice == '2':
            vendor_menu(vendors)
        elif choice == '3':
            po_menu(products, vendors, purchase_orders)
        elif choice == '4':
            report_menu(products, vendors, purchase_orders)
        elif choice == '5':
            save_data(products, vendors, purchase_orders)
        elif choice == '6':
            products, vendors, purchase_orders = load_data()
        elif choice == '7':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice.")

def product_menu(products, vendors):
    """
    Product management submenu.
    Parameters: products (list), vendors (list)
    Returns: None
    """
    while True:
        print("\nProduct Menu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Products")
        print("4. Edit Product")
        print("5. Deactivate Product")
        print("6. Display Low-Stock")
        print("7. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_product(products, vendors)
        elif choice == '2':
            view_products(products)
        elif choice == '3':
            query = input("Enter search query: ").strip()
            results = search_products(products, query)
            for p in results:
                p.display()
        elif choice == '4':
            edit_product(products, vendors)
        elif choice == '5':
            deactivate_product(products)
        elif choice == '6':
            display_low_stock(products)
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

def vendor_menu(vendors):
    """
    Vendor management submenu.
    Parameters: vendors (list)
    Returns: None
    """
    while True:
        print("\nVendor Menu:")
        print("1. Add Vendor")
        print("2. View Vendors")
        print("3. Search Vendors")
        print("4. Edit Vendor")
        print("5. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_vendor(vendors)
        elif choice == '2':
            view_vendors(vendors)
        elif choice == '3':
            query = input("Enter search query: ").strip()
            results = search_vendors(vendors, query)
            for v in results:
                v.display()
        elif choice == '4':
            edit_vendor(vendors)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def po_menu(products, vendors, purchase_orders):
    """
    Purchase order submenu.
    Parameters: products (list), vendors (list), purchase_orders (list)
    Returns: None
    """
    while True:
        print("\nPurchase Order Menu:")
        print("1. Create PO")
        print("2. View POs")
        print("3. Receive Shipment")
        print("4. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            create_purchase_order(products, vendors, purchase_orders)
        elif choice == '2':
            view_purchase_orders(purchase_orders)
        elif choice == '3':
            receive_shipment(products, purchase_orders)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def report_menu(products, vendors, purchase_orders):
    """
    Reports submenu.
    Parameters: products (list), vendors (list), purchase_orders (list)
    Returns: None
    """
    while True:
        print("\nReports Menu:")
        print("1. Full Inventory")
        print("2. Low-Stock")
        print("3. Total Value")
        print("4. Open POs")
        print("5. Received POs")
        print("6. Vendor Report")
        print("7. Export to Text")
        print("8. Back")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            full_inventory_report(products)
        elif choice == '2':
            low_stock_report(products)
        elif choice == '3':
            total_inventory_value_report(products)
        elif choice == '4':
            open_purchase_orders_report(purchase_orders)
        elif choice == '5':
            received_purchase_orders_report(purchase_orders)
        elif choice == '6':
            vendor_report(vendors, products)
        elif choice == '7':
            export_report_to_text(products)
        elif choice == '8':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    products, vendors, purchase_orders = load_data()
    main_menu(products, vendors, purchase_orders)