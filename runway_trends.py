import pandas as pd
import random

# okay this is me making my own little fashion trend dataset
# no API, just vibes & coffee ☕✨

# 🍒 style ideas I like or see trending online
items = [
    ("Denim Mini Skirt", "Bottom", "Blue", "Denim"),
    ("Leather Trench Coat", "Outerwear", "Brown", "Leather"),
    ("Crochet Top", "Top", "White", "Cotton"),
    ("Cargo Pants", "Bottom", "Green", "Cotton"),
    ("Oversized Blazer", "Outerwear", "Black", "Wool"),
    ("Satin Slip Dress", "Dress", "Red", "Satin"),
    ("Platform Boots", "Shoes", "Black", "Leather"),
    ("Bucket Hat", "Accessory", "Beige", "Canvas"),
    ("Puffer Jacket", "Outerwear", "White", "Polyester"),
    ("Maxi Skirt", "Bottom", "Navy", "Silk"),
    ("Knit Vest", "Top", "Grey", "Wool"),
    ("Sheer Blouse", "Top", "Cream", "Silk"),
    ("Tulle Skirt", "Bottom", "Pink", "Tulle"),
    ("Ballet Flats", "Shoes", "Blush", "Leather"),
    ("Techwear Jacket", "Outerwear", "Charcoal", "Nylon"),
    ("Denim Jumpsuit", "One-piece", "Indigo", "Denim"),
    ("Sequin Crop Top", "Top", "Silver", "Sequin"),
    ("Faux Fur Coat", "Outerwear", "Ivory", "Faux Fur"),
    ("Wide-Leg Trousers", "Bottom", "Camel", "Linen"),
    ("Statement Belt", "Accessory", "Gold", "Metal")
]

# seasonal range – SS = spring/summer, FW = fall/winter
# kind of just made these up to cover a few years
seasons = ["SS21", "FW21", "SS22", "FW22", "SS23", "FW23", "SS24", "FW24", "SS25"]

data_rows = []

# loop over each season & item combo to make fake data
for szn in seasons:
    for piece in items:
        pop_score = round(random.uniform(3.5, 9.5), 1)  # 0-10 scale
        buzz_val = random.randint(20, 100)              # like social media mentions
        # mix the two + a little randomness to simulate "trend score"
        trend_score = round((pop_score * 0.55 + buzz_val * 0.045) + random.uniform(-0.5, 0.5), 1)

        row = [szn, *piece, pop_score, buzz_val, trend_score]
        data_rows.append(row)

# 🧃 toss it all into a DataFrame
df = pd.DataFrame(data_rows, columns=[
    "Season", "Trend Item", "Category", "Color", "Fabric",
    "Previous Popularity", "Social Buzz", "Trend Score"
])

# save it out – maybe change the filename later?
df.to_csv("runway_trends.csv", index=False)
print("✅ Done! Your handmade fashion dataset is ready 💅 (runway_trends.csv)")
