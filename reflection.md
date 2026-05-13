# Reflection

## What part of the project was hardest?
The hardest part for me was getting the save/load feature to work properely and making sure the data was loading from the correct spot. 

## What bug took the longest to solve?
Getting all the files to talk to each other took the longest making sure I had the correct immports and data types. Also pythons tab system gives me trouble constantly becuase I am used to other languages where tabs and spaces don't matter. 

## How did you organize your code across multiple files?
I separated concerns: models.py for classes, inventory_manager.py for all product and vendor logic, file_manager.py for save/load logic, reports.py for reporting, and main.py for the UI. 
## How does your save/load system work?
The save system converts objects to dictionaries using to_dict methods and saves to JSON. Load reads the JSON, creates objects using from_dict class methods. It handles file not found gracefully by starting with empty data.

## What would you improve if you had another week?
If I had more time I think adding GUI as I am not a big fan of using the terminal. I also think adding an algorithim to see what items are being sold the fastest based off of how many times a product has been reordered within a certian time frame would be benificial for a business. This could give them a way to see what items are the most popular and potenitally stock more so there is no risk of not having it. 

