import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

# okay deep breath... training the model here
# not perfect but works for now

# 🧵 load my fashion trend data
data = pd.read_csv("runway_trends.csv")

# peek at the data (I keep doing this out of habit lol)
print("\n👀 First few rows:")
print(data.head(3))

# sanity check – are we missing anything?
print("\n🕵️‍♀️ Null value count:")
print(data.isnull().sum())

# ✂️ Features we’ll use (both numbers + categories)
# might add more features later but this is fine for now
features_raw = data[["Previous Popularity", "Social Buzz", "Category", "Color", "Fabric"]]
target = data["Trend Score"]

# one-hot encode the categorical stuff
cat_cols = ["Category", "Color", "Fabric"]
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
cat_encoded = encoder.fit_transform(features_raw[cat_cols])

# 👾 Combine it with numeric features
num_vals = features_raw[["Previous Popularity", "Social Buzz"]].values
X_full = np.hstack((num_vals, cat_encoded))

# 😮 print just to check shape — I always do this
print(f"\n🔢 Encoded features shape: {X_full.shape}")

# train/test split — might try different test sizes later
X_train, X_test, y_train, y_test = train_test_split(
    X_full, target, test_size=0.2, random_state=42
)

# model timeee
model = LinearRegression()
model.fit(X_train, y_train)

# predict on the test set, cross fingers 🤞
y_pred = model.predict(X_test)

# 💅 Performance check (so far so good)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📈 Model evaluation:")
print(f"📉 MAE (mean absolute error): {mae:.2f}")
print(f"📊 R² Score: {r2:.2f}")

# could add visualizations later but I’m lazy rn
# might also save the model but meh
