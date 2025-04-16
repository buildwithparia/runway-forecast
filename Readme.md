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

- 🔥 **Season**: from Spring/Summer 2021 until Spring/Summer 2025  
- 👗 **Trend Item**: like “maxi skirt” or “platform boots”  
- 🧳 **Category**: like “bottom” or “accessory”  
- 👚 **Color**: like “navy” or “blush”  
- 🧵 **Fabric**: like “denim” or “satin”  
- 🌀 **Previous Popularity**:  
  a random number between 3.5 and 9.5 — reflects how popular or wearable a fashion item already is  
  (based on past seasons, general style trends, or just its reputation)  
- 📢 **Social Buzz**:  
  a number from 20 to 100 — represents how much people are talking about the item on IG, TikTok, Pinterest, etc.  
- ✨ **Trend Score**:  
  this is a “vibe” score calculated from all the features above using this formula:

  > *Trend Score = (Popularity × 0.55) + (Buzz × 0.045) + Chaos (±0.5)*


---
I used **one-hot encoding** because I’m working with labels like color and fabric, not numbers.  
It’s better than label or ordinal encoding in this case.

I trained a **linear regression model** because it works well with numerical + encoded features.  
The model did a good job and got these results:

- 📊 **Mean Absolute Error**: 0.27  
- 📊 **R² Score**: 0.96

The model can’t read minds… but I think it works pretty well! 🧙‍♀️



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

## 😵‍💫 Why I did this

I’ve always been curious about combining my interests.  
This project gave me the chance to merge **fashion** with **coding** — and I had a lot of fun doing it.

I also wanted to challenge myself to create something that could reflect both creativity and logic, and maybe even have a little real-world potential.

---

## 🌍 Why this matters

Fashion isn’t just about clothes — it’s about culture, identity, and self-expression.  
And trends? They’re not random — they reflect people’s emotions, needs, moods, and even societal shifts.

A model like this, even in its early form, could one day help:
- Small or independent designers make more confident decisions 💼  
- Sustainable brands avoid overproduction by forecasting likely demand 🌱  
- Retailers and stylists analyze trend movements instead of guessing 🛍️  
- Researchers understand how style spreads across platforms like TikTok or Pinterest 📲

It might be a simple linear model now, but it represents something bigger:
> Using tech to understand people, culture, and what we wear to express who we are.

So yes — I made it to learn. But I also made it to explore something meaningful ✨


---

## 🛠️ might add later

- Try more complex model like random forest or XGBoost
- Expand the dataset and using real-world trend data
- Build a streamlit app and turn it into my own mini pinterest

---

## 🖤 made by

[@buildwithparia](https://github.com/buildwithparia)  
Built by Paria with Python, style, and Pinterest scrolls at 2am 💗

