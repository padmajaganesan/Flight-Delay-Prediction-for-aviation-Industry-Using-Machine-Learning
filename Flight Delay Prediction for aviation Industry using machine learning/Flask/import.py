import pandas as pd
from pandas.conftest import axis

dataset = pd.read_csv(r"C:\Users\TAMIL BOYS\PycharmProjects\flightdata.csv")
dataset.head()

dataset.info()

dataset = dataset.drop('Unnamed: 25', axis=1)
dataset.isnull().sum()

dataset = dataset[
    ["FL_NUM", "MONTH", "DAY_OF_MONTH","DAY_OF_WEEK", "ORIGIN", "DEST", "CRS_ARR_TIME", "DEP_DEL15", "ARR_DEL15"]]
dataset.isnull().sum()

dataset[dataset.isnull().any(axis=1)].head(10)

dataset['DEP_DEL15'].mode()
dataset = dataset.fillna({'ARR_DEL15': 1})
dataset = dataset.fillna({'DEP_DEL15': 0})
dataset.iloc[177:185]
assert isinstance(dataset, object)
print(dataset)

