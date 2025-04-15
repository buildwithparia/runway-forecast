# 🧵 Runway Forecast

One of the most fun experiment during my machine learning journey...sewing fashion and technology 🪡


---
## ❓ what is this?

this started as me wondering:  
> *“what if I could predict what’s gonna be trendy next season?”*

This project predict trend scores for fashion pieces based on their popularity, social buzz and aesthetic elements like fabric, color and category.
It includes:
- A handmade dataset of +180 fashion items across 4 seasons
- A linear regression model trained to learn the ~vibe score~
- A fun prediction for upcoming FW2025 fashion trends

It's not perfect but I'm proud of it. ✨
I'm here to learn and grow not to always be perfect.

---

## ❓ what’s in the project

- `runway_trends.py` → generates the fashion dataset (my fake Vouge universe💫)
- `runway_trends.csv` → the dataset with items, colors, fabrics, popularity, buzz, etc.
- `preprocess_and_train.py` → trains & evaluates the model on trend data
- `predict_fw25.py` → predicts trend scores for totally new FW25 items 🧥🧶

---

## 💻 how it works

Each item has some features:
 👗	Season : from spring/summer 2021 until spring/summer 2025
 👔	Trend item : like “maxi skirt” or “platform boots”
 🧥	Category : like “bottom” or “accessory”
 👚	Color : like “navy” or “blush”
 👖	Fabric : like “denim” or “satin”
 👟	Previous popularity : it’s a random number between 3.5 to 9.5 , it’s a score that reflects how popular or wearable a fashion item already is based on past seasons, general style trends or its reputation
 👜	Social buzz : randomly generated between 20 and 100 , it represents how much people are talking about a fashion item like on IG and pinterest
 🧢	Trend score : this number calculated using a custom formula based on previous popularity, social buzz and a bit of chaos to make it feel more real like this:
                   Trend Score = (Popularity × 0.55) + (Buzz × 0.045) + Chaos (±0.5)

I used one-hot encoding, it’s the best option compare to the label encoding or other types of encoding because I deal with numbers in this project not words.
And trained a linear regression model because it can work very well with numeral and one-hot features.
The model works very well and got these metrics:
🧷	Mean Absolute Error = 0.27
🧷	R2 = 0.96
The model can’t read minds but I think it works good🤷🏻



---

## 🔮 sample prediction output

🔥 FW25 Trend Forecast – Ranked by Predicted Score:  
=================================================  
Rank | Trend Item             | Predicted Score  
-----|------------------------|------------------  
1    | Metallic Puffer        | 8.09  
2    | Maxi Leather Skirt     | 7.48 
3    | Velvet Cape            | 7.01 
4    | Furry Bucket Hat       | 6.15  
5    | Knit Balaclava         | 5.98 

I’d wear at least 3 of these! Not the metallic puffer I now they will be so trendy but not my type! 💅🏻

---

## 😵‍💫 why I did this

I’ve always been curious about combining my interests.
This project let me combine **fashion + coding**, and it turned out to be a great learning experience.
I tried to explain everything in the code so it's easy to follow - because sharing what we learn helps everyone 💞
this was more about learning and having fun than being perfect🌠

---

## 🛠️ might add later

- Try more complex model like random forest or XGBoost
- Expand the dataset and using real-world trend data
- Build a streamlit app and turn it into my own mini pinterest

---

## 🖤 made by

[@buildwithparia](https://github.com/buildwithparia)  
Built by Paria with Python, style, and Pinterest scrolls at 2am 💗
