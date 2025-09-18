from sklearn.impute import KNNImputer
import pandas as pd
data=pd.read_csv(r"C:\Users\hp\Downloads\MISSING_DATASET_HANDLING.csv",encoding='latin1')
print(data.isnull().sum())

imputer = KNNImputer(n_neighbors=5)
data_imputed = pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=[float,int])),
                            columns=data.select_dtypes(include=[float,int]).columns)
print(data.isnull().sum())
