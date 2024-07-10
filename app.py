import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('stock_price_model.pkl')

# Set up the Streamlit interface
st.title('Stock Price Prediction')

st.write('Please enter the details to predict the stock price:')

# Input features
symbol = st.selectbox('Symbol', options=['AAL', 'AAP', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACN', 'ATVI'])
open_price = st.number_input('Open Price')
high_price = st.number_input('High Price')
low_price = st.number_input('Low Price')
volume = st.number_input('Volume')
account_payable = st.number_input('Accounts Payable')
accounts_receivable = st.number_input('Accounts Receivable')
additional_income = st.number_input('Additional Income/Expense Items')
after_tax_roe = st.number_input('After Tax ROE')
capital_expenditures = st.number_input('Capital Expenditures')
capital_surplus = st.number_input('Capital Surplus')
cash_ratio = st.number_input('Cash Ratio')

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'open': [open_price],
    'high': [high_price],
    'low': [low_price],
    'volume': [volume],
    'Accounts Payable': [account_payable],
    'Accounts Receivable': [accounts_receivable],
    'Add\'l income/expense items': [additional_income],
    'After Tax ROE': [after_tax_roe],
    'Capital Expenditures': [capital_expenditures],
    'Capital Surplus': [capital_surplus],
    'Cash Ratio': [cash_ratio],
    'symbol': [symbol]
})

# Convert categorical data to numerical data
input_data = pd.get_dummies(input_data, columns=['symbol'])

# Ensure all columns from the training data are present
for col in features.columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Predict the stock price
prediction = model.predict(input_data)

st.write(f'The predicted stock price is: ${prediction[0]:.2f}')
