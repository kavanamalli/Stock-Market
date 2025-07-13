import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
 

model = load_model(r'D:\STOCK\Stock_Market.keras')

st.header("Stock Market Predictor")


stock = st.text_input('Enter Stock Symbol','IBM')
start = '2020-01-01'
end = '2025-06-01'


data = yf.download(stock, start, end)

st.subheader('Stock Data')
st.write(data)

data_train = pd.DataFrame(data.Close[0: int(len(data)*0.80)])
data_test = pd.DataFrame(data.Close[int(len(data)*0.80): len(data)])


scaler = MinMaxScaler(feature_range=(0,1))

scaled_data_train = scaler.fit_transform(data_train)
scaled_data_test = scaler.fit_transform(data_test)

past_100_days = scaled_data_train[-100:]
scaled_data_test = pd.concat([data_train, data_test], axis=0)
data_test = scaler.fit_transform(data_test)

st.subheader('Price vs MA50')

ma_50_days = data.Close.rolling(50).mean()
fig1 = plt.figure(figsize=(8,6))
plt.plot(ma_50_days, 'r')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig1)

st.subheader('Price vs MA100')

ma_50_days = data.Close.rolling(100).mean()
fig2 = plt.figure(figsize=(8,6))
plt.plot(ma_50_days, 'r')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig2)

st.subheader('Price vs MA50 vs MA150')
ma_150_days = data.Close.rolling(150).mean()
fig4 = plt.figure(figsize=(8,6))
plt.plot(ma_50_days, 'r')
plt.plot(ma_150_days, 'b')
plt.plot(data.Close, 'g')
plt.show()
st.pyplot(fig4)

import numpy as np
x_train = []
y_train = []
for i in range(100, len(data_test)):
    x_train.append(data_test[i-100: i])
    y_train.append(data_test[i, 0])

x_train = np.array(x_train)
y_train = np.array(y_train)

predict = model.predict(x_train)

scale =1/scaler.scale_

predict = predict * scale

y_train =   y_train* scale

st.subheader('Original Price vs Predicted Price')
ma_150_days = data.Close.rolling(150).mean()
fig3 = plt.figure(figsize=(8,6))
plt.plot(predict, 'r' ,label = 'Original Price')
plt.plot(y_train, 'b', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
plt.legend()
st.pyplot(fig3)
