import numpy as np
import pandas as py
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #because here value of y increases as of x
x=np.array([500,800,1000,1200,1500]).reshape(-1,1)#to convert to 2D)
y=np.array([150000,20000,230000,260000,300000])

#here no preprocessing 
model = LinearRegression()
model.fit(x,y)#to create best model
#model parameters
print("Intercept(base_price):",model.intercept_)
print("Slope(price per sqft):",model.coef_[0])
size = 1100 
predicted_price = model.predict([[size]])
print(f"Predicted prize for {size} sqft = ${predicted_price[0]:2f}")

