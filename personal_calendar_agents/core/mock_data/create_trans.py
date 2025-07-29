import os
import random
from datetime import datetime, timedelta
import json

category_groups = [
    {
        "group": "Essentials",
        "categories": [
            ("BigBasket", "Groceries", ["Rice", "Pasta", "Bread", "Eggs", "Milk", "Coffee", "Butter", "Chicken Breast"]),
            ("BigBasket", "Household", ["Toilet Paper", "Laundry Detergent", "Dish Soap", "Handwash", "Floor Cleaner"]),
            ("Nature's Basket", "Groceries", ["Oats", "Juice", "Chocolate", "Honey", "Granola"]),
            ("Reliance Fresh", "Groceries", ["Cucumber", "Tomatoes", "Paneer", "Potatoes", "Spinach"]),
            ("PharmEasy", "Healthcare", ["Paracetamol", "Hand Sanitizer", "Vitamin C", "Face Mask", "Antacid"]),
            ("Apollo Pharmacy", "Healthcare", ["Cough Syrup", "Band Aid", "Glucose", "Skin Cream"])
        ]
    },
    {
        "group": "Lifestyle",
        "categories": [
            ("Flipkart", "Garments", ["T-shirt", "Jeans", "Sweatshirt", "Jacket", "Track Pants", "Socks", "Blazer"]),
            ("Myntra", "Garments", ["Shirt", "Shorts", "Pullover", "Kurta", "Ethnic Dress"]),
            ("Pantaloons", "Garments", ["Cotton Pants", "Kurti", "Dupatta", "Tunic"]),
            ("Nike", "Shoes", ["Running Shoes", "Sneakers", "Flip Flops"]),
            ("Adidas", "Shoes", ["Sports Shoes", "Slippers"]),
            ("Bata", "Shoes", ["Formal Shoes", "Loafers"]),
            ("Westside", "Accessories", ["Belt", "Sunglasses", "Wallet", "Backpack"]),
            ("Archies", "Gifts", ["Greeting Card", "Gift Mug", "Keychain", "Photo Album"])
        ]
    },
    {
        "group": "Leisure",
        "categories": [
            ("Decathlon", "Sports Gear", ["Badminton Racket", "Football", "Yoga Mat", "Skipping Rope"]),
            ("BookMyShow", "Recreation", ["Movie Ticket", "Concert Ticket", "Standup Comedy Show", "Workshop Entry"]),
            ("UrbanClap", "Services", ["Salon at Home", "Massage", "Cleaning Service", "AC Repair"]),
            ("PVR Cinemas", "Recreation", ["Movie Ticket", "Popcorn Combo"]),
            ("Bowling Alley", "Recreation", ["Bowling Session", "Shoe Rental"]),
            ("Makemytrip", "Travel", ["Flight Ticket", "Bus Booking", "Cab", "Travel Insurance"]),
            ("Oyo Rooms", "Travel", ["Hotel Booking", "Weekend Getaway"])
        ]
    },
    {
        "group": "Food & Drink",
        "categories": [
            ("Swiggy", "Outside Food", ["Pizza", "Burger", "Biryani", "Momos", "Fries", "Dosa", "Sandwich", "Sushi"]),
            ("Zomato", "Outside Food", ["Ice Cream", "Milkshake", "Chinese Combo", "Veg Platter"]),
            ("Starbucks", "Coffee", ["Cappuccino", "Mocha", "Sandwich", "Croissant", "Espresso", "Cold Brew"]),
            ("Cafe Coffee Day", "Coffee", ["Cafe Latte", "Classic Coffee", "Egg Puff"]),
            ("Local Liquor Shop", "Liquor", ["Whiskey", "Rum", "Vodka", "Gin", "Beer", "Wine"]),
            ("HipBar", "Liquor", ["Single Malt", "Craft Beer", "Rose Wine"])
        ]
    },
    {
        "group": "Electronics",
        "categories": [
            ("Amazon", "Electronics", ["Bluetooth Speaker", "Wireless Mouse", "Phone Charger", "Smart Watch", "Earphones", "Tablet", "Webcam", "SSD"]),
            ("Croma", "Electronics", ["Laptop", "Monitor", "Wired Keyboard", "Gaming Mouse", "Printer"]),
            ("Apple Store", "Electronics", ["iPhone Case", "Apple Cable", "Power Adapter", "AirPods", "Macbook Sleeve"])
        ]
    },
    {
        "group": "Home & Decor",
        "categories": [
            ("Amazon", "Home Decor", ["Table Lamp", "Cushion Cover", "Wall Clock", "Photo Frame", "Curtain Set"]),
            ("Pepperfry", "Home Decor", ["Bed Sheet", "Sofa Throw", "Wall Art", "Vase"])
        ]
    }
]

def generate_transactions(n=150):
    transaction_list = []
    base_date = datetime.now()

    for i in range(n):
        group = random.choice(category_groups)
        merchant, cat, items = random.choice(group["categories"])
        item = random.choice(items)
        if cat == "Electronics":
            amount = random.randint(999, 14999)
        elif cat == "Garments":
            amount = random.randint(299, 3999)
        elif cat == "Shoes":
            amount = random.randint(799, 7999)
        elif cat in ("Household", "Home Decor"):
            amount = random.randint(129, 2999)
        elif cat == "Groceries":
            amount = random.randint(89, 999)
        elif cat in ("Sports Gear", "Games"):
            amount = random.randint(399, 3599)
        elif cat in ("Recreation", "Travel", "Services"):
            amount = random.randint(299, 3999)
        elif cat == "Liquor":
            amount = random.randint(299, 4999)
        elif cat in ("Coffee", "Outside Food"):
            amount = random.randint(99, 899)
        elif cat == "Healthcare":
            amount = random.randint(79, 699)
        elif cat == "Accessories":
            amount = random.randint(199, 1599)
        elif cat == "Gifts":
            amount = random.randint(99, 999)
        else:
            amount = random.randint(100, 3500)
        days_ago = random.randint(0, 29)
        date = (base_date - timedelta(days=days_ago)).strftime("%Y-%m-%d")

        transaction = {
            "date": date,
            "merchant": merchant,
            "category_group": group["group"],
            "category": cat,
            "item": item,
            "amount": amount
        }
        transaction_list.append(transaction)
    return transaction_list

# Main loop to create different transactions for each agent
path_root = "./data/agents/personal/"

for agent_name in os.listdir(path_root):
    # Skip hidden files/folders if any
    if agent_name.startswith("."):
        continue
    trans = generate_transactions(15)
    with open(os.path.join(path_root, agent_name, "transactions.json"), "w") as f:
        json.dump(trans, f, indent=2)
