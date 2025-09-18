# Employee Salary Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load dataset
df = pd.read_csv("Employers_data.csv")

# 2. Select feature and target
X = df[["Experience_Years"]]   # independent variable
y = df["Salary"]               # dependent variable

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Show the equation of the line
print(f"Model: Salary = {model.coef_[0]:.2f} * Experience_Years + {model.intercept_:.2f}")

# 5. User Input and Prediction
try:
    exp = float(input("\nEnter years of experience: "))
    predicted_salary = model.predict([[exp]])[0]
    print(f"Predicted Salary for {exp} years of experience: {predicted_salary:.2f}")
except ValueError:
    print("Please enter a valid number!")
