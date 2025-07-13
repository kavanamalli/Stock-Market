# 📈 Streamlit Stock Price Predictor

A web-based application built using **Streamlit** and **Keras** that predicts stock prices based on historical data. The app works with **any stock ticker** symbol supported by [Yahoo Finance](https://finance.yahoo.com/), such as `AAPL`, `TSLA`, `IBM`, `RELIANCE.NS`, etc.

---

## 🚀 Features

- 🔍 Input **any valid stock ticker**
- 📈 Fetches historical stock data (from **2020-01-01 to 2025-06-01**)
- 📊 Visualizes:
  - Stock price trend
  - Moving averages: 50, 100, and 150 days
- 🤖 Predicts closing prices using a **deep learning model** (`Stock_Market.keras`)
- 📉 Interactive chart showing actual vs predicted prices
- 🖥️ Lightweight and fast web UI using **Streamlit**

---

## 🗂️ Project Structure

📦 D:\STOCK
┣ 📄 app.py ← Main Streamlit app
┣ 📄 Stock_Market.keras ← Pre-trained Keras model
┣ 📄 README.md ← Project documentation


---

## 📦 Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt

---

## ▶️ How to Run the App
Open terminal or command prompt

Navigate to the project folder:
Launch the Streamlit app:
streamlit run app.py
This will open the app in your browser at:
http://localhost:8501

---

## 🎯 How It Works
User inputs a stock ticker (e.g., AAPL, RELIANCE.NS)

App fetches 10 years of daily data from Yahoo Finance using yfinance

Data is scaled with MinMaxScaler and reshaped for prediction

The trained Keras model loads and predicts future stock prices

Actual and predicted prices are plotted using matplotlib

---

## 📌 Notes
The model uses the previous 100 days of data to make the next price prediction.

Works with all Yahoo Finance stock tickers, including Indian stocks like:

RELIANCE.NS

TCS.NS

INFY.NS

---

## 📷 Sample Output (Optional)
You can find the sample images in Images folder

