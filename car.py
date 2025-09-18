import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#Load dataset
columns = ['buying','maint','doors','persons','lug_boot','safety','class']
df = pd.read_csv(r"C:\Users\hp\Downloads\car.data",names=columns)
print(df)
print(df.isnull().sum()) #here no null values so next step not required
print(df.head())

#Encoding 
df_encoded = pd.get_dummies(df, drop_first=True)
print(df_encoded.head())

#2.Split dataset
df.rename(columns={'buying': 'purchasing'}, inplace=True)
print(df.head())

X = df.drop('purchasing', axis=1)
y = df['persons']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )


print(X.head())
print(y.head())





