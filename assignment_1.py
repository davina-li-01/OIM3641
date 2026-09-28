import datetime as dt

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from stock import Stock

st.set_page_config(page_title="Stock Analysis", layout="wide")
st.title("Stock Analysis App")

@st.cache_data
def load_stock(symbol, start, end, ma_window, ma_window2):
    """Creating a Stock downloads the data, so this is the fetch"""
    return Stock(symbol, start, end, ma_window, ma_window2)


# --- Sidebar (shared by both tabs) ---
st.sidebar.header("Settings")
symbol = st.sidebar.text_input("Ticker symbol", "AAPL").upper().strip()
start = st.sidebar.date_input("Start date", dt.date.today() - dt.timedelta(days=365))
end = st.sidebar.date_input("End date", dt.date.today())
ma_window = st.sidebar.slider("Short moving average window", 5, 200, 20)
ma_window2 = st.sidebar.slider("Long moving average window", 5, 200, 50)

# remember that the button was clicked so the page doesn't reset on every widget change
if st.sidebar.button("Get Data"):
    st.session_state.fetched = True

tab1, tab2 = st.tabs(["Single Stock Analysis", "Portfolio Comparison"])

# --- Tab 1: Single Stock ---
with tab1:
    if not st.session_state.get("fetched"):
        st.info("Choose your settings in the sidebar and click Get Data.")
    else:
        with st.spinner(f"Downloading {symbol}..."):
            stock = load_stock(symbol, start, end, ma_window, ma_window2)

        if stock.data is None:
            st.error(stock.message)
        else:
            st.success(stock.message)
            df = stock.data

            # metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Last Close", f"${df['Close'].iloc[-1]:.2f}",
                        f"{df['change'].iloc[-1]:.2f}")
            col2.metric("Cumulative Return", f"{df['return'].sum():.2%}")
            col3.metric("Trading Days", len(df))

            # price + moving average (the class doesn't have this chart, so build it here)
            fig = px.line(df, x=df.index, y=["Close", "MA", "MA2"],
                          title=f"{symbol} Close Price with {ma_window}-Day and {ma_window2}-Day Moving Averages",
                          labels={"value": "Price ($)", "variable": ""})
            fig.update_layout(hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)
            # note: first ma_window - 1 rows of MA are NaN, so the MA line starts later

            # charts from the class
            st.plotly_chart(stock.plot_performance(), use_container_width=True)
            st.plotly_chart(stock.plot_return_dist(), use_container_width=True)

            # stats table
            st.subheader("Return Statistics")
            st.dataframe(df["return"].describe())

# --- Tab 2: Portfolio Comparison ---
with tab2:
    tickers_input = st.text_input("Enter tickers separated by commas", "AAPL, MSFT, GOOG")
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

    if st.button("Compare"):
        st.session_state.compared = True

    if st.session_state.get("compared"):
        performance = {}
        with st.spinner("Downloading portfolio data..."):
            for ticker in tickers:
                s = load_stock(ticker, start, end, 10, 50)  # MA not used here
                if s.data is None:
                    st.error(s.message)
                    continue  # skip this one, keep going
                cum = s.data["return"].cumsum()
                performance[ticker] = cum - cum.iloc[0]  # zero-based: every line starts at 0.0

        if performance:
            perf_df = pd.DataFrame(performance)
            fig = px.line(perf_df, x=perf_df.index, y=perf_df.columns,
                          title="Cumulative Performance Comparison",
                          labels={"value": "Cum Return", "index": "Date", "variable": "Ticker"})
            fig.add_hline(y=0, line_dash="dash", line_color="black", opacity=0.7)
            fig.update_layout(yaxis_tickformat=".1%", hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)

            st.caption("Starting values (should all be 0.0):")
            st.write(perf_df.iloc[0])