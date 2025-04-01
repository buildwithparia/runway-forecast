import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

# okay... predicting trend scores for FW25, let's go
# this is just a fun experiment tbh, might change stuff later 🤷‍♀️

# load the OG trend dataset
df = pd.read_csv("runway_trends.csv")

# not sure if this is the best way but we rollin' with it
cat_cols = ["Category", "Color", "Fabric"]

# encoder setup — IMPORTANT: don't crash on new stuff like 'Burgundy'
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoder.fit(df[cat_cols])  # reusing encoder from training-ish

# raw inputs for model, same as before
Xstuff = df[["Previous Popularity", "Social Buzz"] + cat_cols]
y = df["Trend Score"]  # what we're trying to predict

# split things up manually cause I like it like this
num_features = Xstuff[["Previous Popularity", "Social Buzz"]].values
cat_features = encoder.transform(Xstuff[cat_cols])
features_encoded = np.hstack((num_features, cat_features))

# train the model (yes again, I didn’t save it earlier lol)
model = LinearRegression()
model.fit(features_encoded, y)

# okay here’s where we define the new FW25 items
# just made-up ideas I think are cool rn
new_items = [
    {"Trend Item": "Velvet Cape", "Category": "Outerwear", "Color": "Burgundy", "Fabric": "Velvet", "Previous Popularity": 6.8, "Social Buzz": 72},
    {"Trend Item": "Metallic Puffer", "Category": "Outerwear", "Color": "Silver", "Fabric": "Polyester", "Previous Popularity": 7.5, "Social Buzz": 88},
    {"Trend Item": "Furry Bucket Hat", "Category": "Accessory", "Color": "Cream", "Fabric": "Faux Fur", "Previous Popularity": 6.0, "Social Buzz": 65},
    {"Trend Item": "Maxi Leather Skirt", "Category": "Bottom", "Color": "Black", "Fabric": "Leather", "Previous Popularity": 7.1, "Social Buzz": 80},
    {"Trend Item": "Knit Balaclava", "Category": "Accessory", "Color": "Charcoal", "Fabric": "Wool", "Previous Popularity": 5.9, "Social Buzz": 60}
]

# throwing them into a DataFrame bc why not
future_df = pd.DataFrame(new_items)

# encode + merge just like above
new_cat = encoder.transform(future_df[cat_cols])
new_num = future_df[["Previous Popularity", "Social Buzz"]].values
X_pred = np.hstack((new_num, new_cat))

# run predictions
trend_predictions = model.predict(X_pred)
future_df["Predicted Trend Score"] = trend_predictions

# sort it — I want the most hyped at the top
future_df = future_df.sort_values(by="Predicted Trend Score", ascending=False)

# debug print I might remove later
# print(future_df[['Trend Item', 'Predicted Trend Score']])

# 🎯 Final Output
print("\n🔥 FW25 Trend Forecast – Ranked by Predicted Score:")
print("=" * 65)
print(f"{'Rank':<5}{'Trend Item':<25}{'Predicted Score':<20}")
print("-" * 65)

# just printing in ranked order manually
for i, row in future_df.iterrows():
    print(f"{i+1:<5}{row['Trend Item']:<25}{row['Predicted Trend Score']:.2f}")

# TODO: maybe add visuals later?
