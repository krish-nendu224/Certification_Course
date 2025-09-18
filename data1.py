# import pandas as py
# from sklearn.model_selection import train_test_split #splitting datas to train and test eg:covide +ve ,-ve
# from sklearn.linear_model import LogisticRegression#algorithm
# from sklearn.metrics import accuracy_score,classification_report,confusion_matrix #accuracy test aakan
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = py.read_csv(r"C:\Users\hp\Downloads\50_startups_sample.csv")
# #print(data.head())
# #print(data.info())

# df = pd.DataFrame(data.data, columns=data.features_names)
# df["profit"] = data.profit




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression#numeric value predict
from sklearn.metrics import r2_score, mean_absolute_error#r2=evaluate
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns



# 1. Load dataset (raw string for Windows path)
df = pd.read_csv(r"C:\Users\hp\Downloads\50_startups_sample.csv", encoding='latin1')

# Features and Target
X = df.drop(columns=["Profit"])
y = df["Profit"]



# Encode categorical variable "State"
categorical_features = ["State"]
numeric_features = [col for col in X.columns if col not in categorical_features]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(drop="first", handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numeric_features)
    ]
)



# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build pipeline (preprocessing + model)
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train model
model.fit(X_train, y_train)



# Predictions
y_pred = model.predict(X_test)

print("Model R² Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# Scatter plot: Actual vs Predicted
plt.figure(figsize=(6,5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Actual vs Predicted Profit")
plt.show()



print("\n--- Profit Prediction ---")

rd_spend = float(input("Enter R&D Spend: "))
admin = float(input("Enter Administration Spend: "))
marketing = float(input("Enter Marketing Spend: "))
state = input("Enter State (e.g. 'New York', 'California', 'Florida'): ")

# Create DataFrame for user input
user_data = {
    "R&D Spend": rd_spend,
    "Administration": admin,
    "Marketing Spend": marketing,
    "State": state
}
user_df = pd.DataFrame([user_data])

# Predict Profit
predicted_profit = model.predict(user_df)[0]
print(f"\n Predicted Profit: ${predicted_profit:.2f}")
