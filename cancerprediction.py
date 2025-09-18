import pandas as py
from sklearn.datasets import load_breast_cancer #to load predefined data 
from sklearn.model_selection import train_test_split #splitting datas to train and test eg:covide +ve ,-ve
from sklearn.linear_model import LogisticRegression# yes or no prediction
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix #accuracy test aakan
import seaborn as sns
import matplotlib.pyplot as plt

#Load dataset
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.features_names)#dataframe - to make data in rows and columns
df["target"] = data.target #0 = malignant,1= benign

df_small = df[["mean radius","mean texture","mean perimeter","mean area","mean smoothness","target"]]#to predict

#2.Split dataset
x = df_small.drop(columns=["target"])
y = df_small["target"]
x_train, x_test, y_train,y_test = train_test_split(
x, y, test_size=0.2, random_state=42,stratify=y
)

#3 Train Logistic Regression
model = LogisticRegression()load algorithm
model.fit(x_train,y_train)

#supervised learning - input & output clear ahn
#unsupervised - 
#4 Evaluation
y_pred = model.predict(x_test)
y_prob = model.predict_prob(x_test)[:,1]
print("Model Accuracy:")

