# 🧵 Runway Forecast

okay so... I tried to predict fashion trends using Python and it kinda worked?? 💅

---

## ❓ what is this?

this started as me wondering:  
> *“what if I could predict what’s gonna be trendy next season?”*

so I made a mini dataset of fashion items over the past few years (fake-ish but based on real vibes), then trained a machine learning model to predict which ones might blow up in **Fall/Winter 2025**.

it's not perfect but I'm proud of it.  
it's ✨aesthetic meets data science✨.

---

## ❓ what’s in the project

- `runway_trends.py` → script to generate my fashion trend dataset (completely made up lol)
- `runway_trends.csv` → the dataset with items, colors, fabrics, popularity, buzz, etc.
- `preprocess_and_train.py` → trained a linear regression model. kinda works shockingly well??
- `predict_fw25.py` → gives me a ranked list of what might trend in FW25 🧥🧶

---

## 💻 how it works

- each item has:
  - season (`SS21` to `SS25`)
  - trend item (like “Velvet Cape” or “Metallic Puffer”)
  - category, color, fabric
  - past popularity score (randomized-ish)
  - social media buzz (randomly generated between 20 and 100)
  - and a made-up trend score

- I used one-hot encoding for the categorical stuff
- combined with numerical features (`Previous Popularity`, `Social Buzz`)
- trained a linear regression model using `scikit-learn`
- model got like 0.28 MAE and 0.95 R² so... not bad?? 🤷‍♀️

---

## 🔮 sample prediction output

🔥 FW25 Trend Forecast – Ranked by Predicted Score:  
=================================================  
Rank | Trend Item             | Predicted Score  
-----|------------------------|------------------  
1    | Metallic Puffer        | 8.03  
2    | Maxi Leather Skirt     | 7.45  
3    | Velvet Cape            | 6.99  
4    | Furry Bucket Hat       | 6.22  
5    | Knit Balaclava         | 6.07  

I’d wear at least 3 of these tbh.

---

## 😵‍💫 why I did this

idk I like fashion and I wanted to do something that wasn’t just another boring ML tutorial. 
I also tried to explain everything in the code comments to make it easier for others to understand (we gotta help each other out, right? 💞)
plus I didn’t feel like scraping real trend data so I made my own ✨fake Vogue universe✨

this was more about learning and having fun than being perfect.

---

## 🛠️ might add later

- graphs?? like trend score over time or smth
- a Streamlit interface would be cute
- actual data from Pinterest or Google Trends (if I feel brave)
- a better model (maybe??)
- saving the model properly lol

---

## 🖤 made by

[@buildwithparia](https://github.com/buildwithparia)  
aka a tired human who likes cute code and cute clothes.
