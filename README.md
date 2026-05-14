# Inventory Management System

## Project Description
This is a inventory management program for a small business. It allows managing products, vendors, purchase orders, tracking stock levels, identifying low-stock items, creating purchase orders, receiving shipments, updating inventory, and generating various reports. The program saves and loads all data using JSON files.

## Features
- **Product Management**: Add, view, search, edit, and deactivate products.
- **Vendor Management**: Add, view, search, and edit vendors.
- **Purchase Order System**: Create POs, view them, and receive shipments.
- **Reports**: Full inventory, low-stock, total value, open/received POs, vendor report.
- **Data Persistence**: Save and load data to/from JSON.

## Required Files
- main.py: Main menu and program entry point.
- models.py: Class definitions for Product, Vendor, PurchaseOrder.
- inventory_manager.py: Core functions for inventory and PO management.
- file_manager.py: Functions for saving and loading data.
- reports.py: All reporting functions.
- README.md: This file.
- inventory_data.json: Created by the program for saving data.


## Instructions for Running the Program
1. Ensure Python 3.x is installed.
2. Run `python main.py` from the project directory.
3. Use the menus to navigate and perform actions.
4. Data is automatically loaded on start if inventory_data.json exists.
5. Save data manually or it will be saved when exiting.

## Data Storage
Data is stored in JSON format in `inventory_data.json`. Products, vendors, and purchase orders are serialized to dictionaries and saved. On load, they are deserialized back into objects.

## Extra Features
- Export report to text file: Allows exporting the full inventory report to a text file for external use.

## Author
Dylan Terry