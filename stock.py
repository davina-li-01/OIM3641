from datetime import date,timedelta
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import yfinance as yf
# CHANGED: deleted "from fontTools.subset import usage"


class Stock:
    def __init__(self,symbol, start=None, end=None, ma_window: int=10):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.ma_window = ma_window
        self.data, self.message = self.get_data()  # CHANGED

    def get_data(self):
        try:
            data = yf.download(tickers=self.symbol,  # CHANGED
                               start=self.start,
                               end=self.end,
                               progress=False,
                               multi_level_index=False)
            if data.empty:
                return None, f"No data for {self.symbol}"
            data = self._calc_returns(data)  # CHANGED
            data['MA'] = self.calc_MA(data)
            return data, f"Successfully downloaded for {self.symbol}"
        except Exception as e:
            return None, f"Failed due to {e}"

    def _calc_returns(self,df):
        df['change'] = df['Close'] - df['Close'].shift(1)  # CHANGED
        df['return'] = np.log(df['Close']).diff().round(4)
        return df.dropna()

    def calc_MA(self,df):
        df['MA' = df['Close'].rolling(window=self.ma_window).mean()]

    def plot_return_dist(self):
        mean_return = self.data['return'].mean
        fig = pxhistogram(self.data['return'],
                          nbins=35,
                          title=f" Distribution of daily returns for {self.symbol}",
                          labels={'value':'Return','count':'Frequency'})
        fig.update_traces(marker_line_color='rgb(255,0,0)',
                          marker_line_width=0.5)
        fig.add_vline(x=mean_return,
                      line_dash='dash',
                      line_color='red',
                      annotation_text= f"Mean: {mean_return:.2f}",
                      annotation_position='top right')


# --- For development testing only ---

def main():
    test = Stock(symbol= "AAPL", start= "2025-09-24", end= "2050-09-24")
    print(test.symbol)
    print(test.message)
        fig = test.plot_return_dist()
        fig.show()

if __name__ == "__main__":
    main()