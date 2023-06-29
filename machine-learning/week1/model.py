import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
df = pd.read_csv('new1.csv')
from sklearn.model_selection import train_test_split
x = df.drop(columns=['Price ($)'])
y = df['Price ($)']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=0)
model = LinearRegression().fit(x_train,y_train)
brr = ['Samsung',
 'Motorola',
 'Xiaomi',
 'Realme',
 'Sony',
 'LG',
 'Oppo',
 'CAT',
 'Google',
 'Nokia',
 'OnePlus',
 'Asus',
 'Blackberry',
 'Vivo',
 'Apple',
 'Huawei']

brand = brr.index(input("Enter the brand:").lower().capitalize())
storage = int(input("Enter Storage in GB:"))
ram  = int(input("Enter ram in GB:"))
ssize = float(input("Enter screen size in inchs:"))
cam = int(input("Enter total camera resolution(sum):"))
bat = int(input("Enter battery in mah:"))
k = model.predict([[brand,storage,ram,ssize,cam,bat]])
print(int(k[0]))
