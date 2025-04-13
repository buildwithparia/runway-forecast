#and finally our last step 
# predicting vibes for FW25 – let’s manifest some fashion wins 🧥✨
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder


# grab the full trend dataset that we created earlier
df = pd.read_csv("runway_trends.csv")

# just doing it the same way as before 
categoricals = ["Category", "Color", "Fabric"]

# encoder setup – ignore weird new combos like “Velvet + Burgundy” 
# as we mentioned earlier it's essential
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
# this is where the encoder learns all the possible categories in each column
# it's like saying "hey encoder go look through the category,color and fabric columns and figure out which unique values exist in each "
encoder.fit(df[categoricals])  

# well x_raw now holds everything our model needs to understand a fashion item in one neat package
X_raw = df[["Previous Popularity", "Social Buzz"] + categoricals]
# here's the final vibe score of easch look. The thing we're trying to predict with our model
y_actual = df["Trend Score"]

# well now we grab our numeric columns and turns the pandas dataframe into NumPy array
# we said this before that sklearn loves NumPy, remember?
numeric_bits = X_raw[["Previous Popularity", "Social Buzz"]].values
# here we transfer our categorical features, this gives us a big ol' one-hot matrix of 0s & 1s
# it's like we are turning "satin" & "red" to math📏
cat_bits = encoder.transform(X_raw[categoricals])
# we are combining numerical and categorical data into one single matrix
# this is what we feed into the model
X_features = np.hstack((numeric_bits, cat_bits))

# training the model... again
model = LinearRegression()
model.fit(X_features, y_actual)

# new season drop! totally made-up
# A list of dictionaries where each dictionary represents one fashion item we want to predict the trend score for
fw25_items = [
    {"Trend Item": "Velvet Cape", "Category": "Outerwear", "Color": "Burgundy", "Fabric": "Velvet", "Previous Popularity": 6.8, "Social Buzz": 72},
    {"Trend Item": "Metallic Puffer", "Category": "Outerwear", "Color": "Silver", "Fabric": "Polyester", "Previous Popularity": 7.5, "Social Buzz": 88},
    {"Trend Item": "Furry Bucket Hat", "Category": "Accessory", "Color": "Cream", "Fabric": "Faux Fur", "Previous Popularity": 6.0, "Social Buzz": 65},
    {"Trend Item": "Maxi Leather Skirt", "Category": "Bottom", "Color": "Black", "Fabric": "Leather", "Previous Popularity": 7.1, "Social Buzz": 80},
    {"Trend Item": "Knit Balaclava", "Category": "Accessory", "Color": "Charcoal", "Fabric": "Wool", "Previous Popularity": 5.9, "Social Buzz": 60},
]

# dump it into a DataFrame
# it's structured and ready for encoding and prediction
future_fits = pd.DataFrame(fw25_items)

# same encoding process as before
new_cat_data = encoder.transform(future_fits[categoricals])
new_num_data = future_fits[["Previous Popularity", "Social Buzz"]].values
X_new = np.hstack((new_num_data, new_cat_data))

# make predictions 🎯
predicted_scores = model.predict(X_new)
future_fits["Predicted Trend Score"] = predicted_scores

# ranking magic! it's like tell me which FW25 pieces are going to slay the most💅
future_fits = future_fits.sort_values(by="Predicted Trend Score", ascending=False)

# pretty print results like a lil leaderboard
print("\n🔥 FW25 Trend Forecast – Ranked by Predicted Score:")
print("=" * 65)
print(f"{'Rank':<5}{'Trend Item':<25}{'Predicted Score':<20}")
print("-" * 65)

for idx, row in future_fits.iterrows():
    print(f"{idx + 1:<5}{row['Trend Item']:<25}{row['Predicted Trend Score']:.2f}")

# TODO: maybe plot this later with matplotlib or seaborn? 👀
