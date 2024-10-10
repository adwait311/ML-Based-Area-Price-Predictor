# solve the problem using Linear Regression

# import the lib
import pandas as pd
from sklearn.linear_model import LinearRegression

# load the data
data = pd.read_csv("hpnov23.csv")
print(data)

# feature and target
feature = data[["area"]]
target = data[["price"]]

# model
model = LinearRegression()
model.fit(feature.values, target)

# predict
area = float(input("enter area : "))
price = model.predict([[area]])
print("price = ", price)