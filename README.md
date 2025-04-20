
# 🧵 Runway Forecast

One of the most fun experiments during my ML journey… sewing fashion and code at 2 AM 🪡✨

---

## ❓ What is this?

It all started when I wondered:  
> “What if I could predict next season’s hottest fashion pieces?”

So I mashed together popularity, social buzz, and aesthetic vibes to build a **Trend Score** model.  
It’s a linear regression that (mostly) tells me which runway looks will slay—and which might flop 🙈

Not perfect, but very *me*. It was about learning and vibing, not building a startup.

---

## 📂 What’s in this Repo

- `runway_trends.py` → the script that generates the dataset (my fake Vogue moment)
- `runway_trends.csv` → 180+ items with season, fabric, buzz, and more
- `preprocess_and_train.py` → training pipeline with one-hot encoding & model fitting
- `predict_fw25.py` → forecast FW2025 scores from new fashion entries
- `requirements.txt` → (yeah I still need to commit this 😅)
- `LICENSE` → just in case someone takes this too seriously

---

## 💻 How It Works

1. Create items like "Maxi Skirt", assign features like fabric, color, popularity, buzz.
2. One-hot encode categorical features.
3. Train a **linear regression** model with `scikit-learn`.
4. Predict trend scores using this formula:

```python
Trend Score = (Popularity × 0.55) + (Buzz × 0.045) + Chaos (±0.5)
```

It’s simple, but works surprisingly well:
- MAE: ~0.27
- R² Score: ~0.96

---

## 🔮 Sample Output

```text
🔥 FW25 Trend Forecast:
1    Metallic Puffer        8.09
2    Maxi Leather Skirt     7.48
3    Velvet Cape            7.01
4    Furry Bucket Hat       6.15
5    Knit Balaclava         5.98
```

I’d rock at least three of these. The metallic puffer tho… not sure she’s my vibe 😅

---

## 💡 Why I Made This

Fashion + tech = me.

I wanted to explore how trends reflect culture, moods, and identity — and how a model could *kind of* understand that.

Also, it was just fun. I got to play data scientist *and* fashion editor in the same night.

---

## 🌍 Real-World Potential

This could help:
- Indie designers make better choices
- Sustainable brands avoid overproduction
- Stylists and analysts predict demand instead of guessing

One day, I’d love to add:
- A better model like XGBoost or Random Forest
- Actual real-world data
- A streamlit app that looks like Pinterest but smarter

---

## 👩🏻‍💻 Made by Paria

[@buildwithparia](https://github.com/buildwithparia)  
Built at midnight with tea, Python, and fashion daydreams 💅
