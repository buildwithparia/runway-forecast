
#well after creating the dataset is the time to picking some features and train the model

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

# alright... deep breath 😅 
# not the cleanest setup ever but it's my style

# 👗 loading the trend dataset I made earlier
df = pd.read_csv("runway_trends.csv")

# I just always like checking the top
print("\n👀 Sample rows:")
print(df.head(3)) #3 of them is enough 

# we need to always check if there is a missing value or not
# Even supermodels can't slay without clean data 💁‍♀️ (yes that was a fashion pun 👀)
print("\n🚨 Nulls?? (pls no):")
print(df.isnull().sum())

# picking some features - always remember choose the most related one not just the random stuff
# might add more later if I get curious
raw_features = df[["Previous Popularity", "Social Buzz", "Category", "Color", "Fabric"]]
target_vals = df["Trend Score"]

# okay here we encode our data. it's an essential because we want to transform categorical data into a format that ML models can easily understand and use
# and yeah, I use one-hot encoding because ML models only deal with numbers — not words
#label encoding isn't suitable for nomial data
#ordinal encoding isn't suitable too because we don't have a order
categoricals = ["Category", "Color", "Fabric"]
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')  # don't break on weird values
encoded_cats = encoder.fit_transform(raw_features[categoricals])

# combine numeric + encoded bits
# well now we grab numeric values and trun them into NumPy array because sklearn love NumPy more than pandas
#why? I tell you ( because I like to explain everything in case of someone need it)
#first of all NumPy is pandas older sister so sklearn's core functions were built to expect NumPy arrays
#second sklearn just want numbers but pandas dataframes have labels,column names,etc it's actually good for human but not for models
numerics = raw_features[["Previous Popularity", "Social Buzz"]].values
X = np.hstack((numerics, encoded_cats))

# I always print shapes, it's just a habit and you know it's the quickest sanity check to check everything combined in the right way
print(f"\n📐 Feature matrix shape: {X.shape}")

# split it up! we split our data into 2 sets, one training set and one testing set and we said to use 20% of our data as testing set
# but we can use other numbers too! but this 20/80 is a popular default
X_train, X_test, y_train, y_test = train_test_split(
    X, target_vals, test_size=0.2, random_state=42
)

# linear model feels chill for now! 
# linear regression is fast,easy and gives us a baseline and it works well with numeric + one-hot features
# we can use other models too, we can upgrade ours to random forests
model = LinearRegression()
model.fit(X_train, y_train)

# okay let’s see how this goes... 
y_pred = model.predict(X_test)

# some metrics that basic but important! this is our model report card!
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Results:")
print(f"👉 Mean Absolute Error: {mae:.2f}") #It's the average amount your predictions are off, if it's 0 well our model can read minds! if it's low it's really good but when it's high so we might need to improve girl
print(f"👉 R² Score: {r2:.2f}") #It's coefficient of determination, it measures how well our predictions explain the variance in the data, in my language how much of the trend score magic did I capture?

# NOTE: didn’t save the model yet, maybe later if this turns out useful
#TODO: might add visual plots someday