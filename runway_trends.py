#well well well! welcome to my fashion show!
#first step is making our dataset, we need to feed our future model
import pandas as pd
import random

# okay so this is just me making my fake vogue ☕💅
# It's way better if I had access to real-life database but well...🚶‍♀️

# 🌈 trend pieces I’ve seen all over my feed and pinterest that give ~main character energy~
style_pieces = [
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
    ("Statement Belt", "Accessory", "Gold", "Metal"),
]

# I kinda just made these up to span a few seasons – could expand later
seasons_list = ["SS21", "FW21", "SS22", "FW22", "SS23", "FW23", "SS24", "FW24", "SS25"]

fashion_data = []  # gonna fill this with fake but fabulous rows

# well we have to make our dataset. but how? we create a loop that go through each season+item and giving it a vibe score
for season in seasons_list:
    for item in style_pieces:
        # popularity is like general likability or wearability
        popularity_score = round(random.uniform(3.5, 9.5), 1) #I want to avoid totally hated items and I think every piece is kinda wearable so I concider 3.5 as minimum

        # buzz = how much peopl are *talking* about it, like on TikTok or IG or pinterest
        social_buzz = random.randint(20, 100)

        # here it's the time to mash them together for a ~trend score~
        vibe_score = (popularity_score * 0.55) + (social_buzz * 0.045)
        vibe_score += random.uniform(-0.5, 0.5)  # sprinkle in a little chaos
        vibe_score = round(vibe_score, 1)

        # and here all of our individual ingredients come together into a structured format
        # kinda heart of our dataset building magic ✨
        entry = [season] + list(item) + [popularity_score, social_buzz, vibe_score]
        fashion_data.append(entry)

# This line is like putting our data in a spreadsheet and giving each column its name tag so we can gaze upon our creation🎀
df = pd.DataFrame(fashion_data, columns=[
    "Season", "Trend Item", "Category", "Color", "Fabric",
    "Previous Popularity", "Social Buzz", "Trend Score"
])

# write it to a file – name might change later if I make new versions!
df.to_csv("runway_trends.csv", index=False)

# feels good, honestly
print("✅ Done! Your handmade fashion dataset is ready 💅 (runway_trends.csv)")
