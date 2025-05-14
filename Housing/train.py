# save_model.py
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

housing = pd.read_csv('Housing/Housing.csv')
X = housing.drop("price", axis=1)
y = housing["price"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
test_score = model.score(X_test, y_test)
print(f"Test score: {test_score:.2f}")

with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)
