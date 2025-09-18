import pandas as pd
data=pd.read_csv(r"C:\Users\hp\Downloads\MISSING_DATASET_HANDLING.csv",encoding='latin1')
print(data.isnull().sum())
#null values

data =data.drop(columns=["ADDRESSLINE2"])
print(data.isnull().sum())#to delete this column because of more null values

data=data.dropna(subset=["ORDERDATE","PRODUCTLINE"])#to delete rows of null values
print(data.isnull().sum())

data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median())#fill null values with median
data["YEAR_ID"] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
print(data.isnull().sum())

data["STATUS"].fillna(data["STATUS"].mode()[0],inplace=True)
print(data.isnull().sum())

data["PHONE"].fillna("Unknown",inplace=True) #to fill phoneno null values with unknown
print(data.isnull().sum())