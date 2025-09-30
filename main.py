from pyscript import display
#Restaurant Ordering System using Python Data Types

#String Data Type
restaurant_name = "Pearly Purple"
owner_name = "AACA"

#Integer Data Type
year_since = 2010

#Float Data Type
tax_rate = 0.08

#Boolean Data Type
has_delivery = True
is_dine_in = True
is_takeaway = True

#List Data Type
product_names =["Pain au chocolat", "Garlic Bread", "Sourdough sandwich"]
beverages = ["Sparkling Water", "Hot Tea"]

#Tuple Data Type
business_hours = ("11:00 AM", "9:30 PM")

#Dictionary Data Types
menu = {
    "Pain au Chocolat": 100,
    "Garlic Bread": 125.00,
    "Sourdough Sandwhich": 150.00,
    "Sparkling Water": 50.00,
    "Hot Tea": 35.00
}

#Set Data Types
common_allergens = {"nuts", "dairy", "gluten"}

#Displaying Restaurant Information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")


#Display Menu Items
display(product_names[0], target="prod1")
display(f"₱{menu['Pain au Chocolat']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Garlic Bread']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Sourdough Sandwhich']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Sparkling Water']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Hot Tea']:.2f}", target="price5")


#Display Additional Information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")
display(f"Dine-in Available", target="orderType")
