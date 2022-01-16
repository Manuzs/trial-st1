import streamlit as st
import yfinance as yf
import pandas as pd
st.title("Stoqoute")
st.write("""
## Stock Quotes
 """)
#selecting time period argumnet for ticker history
timeint = pd.array(['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'], dtype = str)
select_time = st.selectbox("Select Time Period", timeint)

#selecting time interval argumnet for ticker history
time_interval_array = pd.array(['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'], dtype = str)
time_interval_select = st.selectbox("select a time interval", time_interval_array)
# selecting ticker symbol
stq = pd.array(['COALINDIA.NS','KOTAKBANK.NS','MARUTI.NS','HINDALCO.NS','BAJFINANCE.NS','INDUSINDBK.NS'], dtype = str)
option = st.selectbox("Select Stock", stq )
st.write("you selected: ", option)

tickerData = yf.Ticker(option)

# getting tickerData
tickerDf = tickerData.history(period = select_time, interval=time_interval_select )

st.line_chart(tickerDf.Close )
st.line_chart(tickerDf.Open)
st.write(type(yf.Ticker(option)))