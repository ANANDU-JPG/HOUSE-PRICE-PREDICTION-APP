
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "size": [800, 1000, 1200, 1500, 1800, 2000],
    "bedrooms": [2, 2, 3, 3, 4, 4],
    "price": [100000, 120000, 150000, 180000, 220000, 250000]
}
df = pd.DataFrame(data)
X = df[["size", "bedrooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Training complete.")
print("Model score:", model.score(X_test, y_test))


with open("house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as house_price_model.pkl")

