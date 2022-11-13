import os
import sys
from os.path import exists

import pandas as pd
import numpy as np
import streamlit as st
import millify
from sqlalchemy import create_engine
from binance.client import Client
from datetime import datetime, timedelta

import config

# Initiate Binance Client
client = Client()

# Initiate database engine
engine = create_engine(config.DB_ENGINE)

# Streamlit inputs
coin = st.selectbox('Coin:', config.TICKERS)
timeframe = st.selectbox('Timeframe:', config.TIMEFRAMES, index=config.TIMEFRAMES.index(config.DEFAULT_TIMEFRAME))

now = datetime.utcnow()

start_at = now - timedelta(days=7)

start = st.date_input('Inicio', start_at)
end_date = st.date_input('Fin', now)


# DEFINICIÓN DE FUNCIONES
def fetch_klines(symbol, timeframe, start_date: str = None, end_date: str = None, keep_last: bool = True):
    #st.write(symbol, timeframe, start_date, end_date)
    #return pd.DataFrame.empty
    klines = client.get_historical_klines(symbol=symbol,interval=timeframe, start_str=start_date, end_str=end_date)
    df = pd.DataFrame(klines)
    if df.empty:
        raise Exception('OHLCV is empty')
    df = df.iloc[:,0:6]
    df.columns = ['Timestamp','Open','High','Low','Close','Volume']
    df['Timestamp'] = pd.to_datetime(df['Timestamp'],unit='ms')
    df.set_index('Timestamp',inplace=True)
    df = df.astype(float)
    if not keep_last:
        df.drop(df.tail(1).index, inplace=True)  # drop last row
    return df


data = fetch_klines(coin, timeframe, str(start), str(end_date))
data.dropna()
# Streamlit as line chart
st.line_chart(data.Close)