import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

# --- AUTO REFRESH ---
st_autorefresh(interval=60 * 1000, key="refresh")

st.title("📊 Live Market Dashboard")

# =========================
# 📈 REAL MARKET DATA
# =========================
data = yf.download("AAPL", period="1mo", interval="1d")

data = data.reset_index()

# --- Chart ---
fig = px.line(data, x="Date", y="Close", title="AAPL Price")
st.plotly_chart(fig, use_container_width=True)

# =========================
# 📊 METRICS
# =========================
returns = data["Close"].pct_change().dropna()

latest_price = data["Close"].iloc[-1]
daily_return = returns.iloc[-1]
volatility = returns.std()

col1, col2, col3 = st.columns(3)

col1.metric("Price", f"${latest_price:.2f}")
col2.metric("Daily Return", f"{daily_return*100:.2f}%")
col3.metric("Volatility", f"{volatility*100:.2f}%")

# =========================
# 💼 PORTFOLIO
# =========================
st.subheader("💼 Portfolio")

tickers = ["AAPL", "MSFT"]

assets = yf.download(tickers, period="1mo")["Close"]

returns_assets = assets.pct_change().dropna()

weights = np.array([0.5, 0.5])
portfolio_returns = returns_assets.dot(weights)

portfolio_value = (1 + portfolio_returns).cumprod()

st.line_chart(portfolio_value)

# =========================
# ⚠️ RISK METRICS
# =========================
st.subheader("⚠️ Risk Metrics")

volatility_port = portfolio_returns.std()
sharpe = portfolio_returns.mean() / volatility_port

col4, col5 = st.columns(2)

col4.metric("Portfolio Volatility", f"{volatility_port*100:.2f}%")
col5.metric("Sharpe Ratio", f"{sharpe:.2f}")