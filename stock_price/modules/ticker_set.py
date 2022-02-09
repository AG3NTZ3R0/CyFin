import pandas as pd
import yfinance as yf


class TickerSet:
    """Represent a set of ticker symbols."""

    def __init__(self, set_name, src_path, ticker_col):
        """Initialize attributes."""
        self.set_name = set_name
        self.df = pd.read_csv(src_path)
        self.ticker_list = self.df[ticker_col].to_list()
        with open(f"../CyFin/stock_price/ticker_lists/{self.set_name}_tickers.txt", 'w') as ticker_file:
            ticker_file.write(' '.join(self.ticker_list))

    def generate_hist_dataset(self):
        """Create a dataset for each ticker symbol in the ticker_list."""
        for ticker in self.ticker_list:
            path = f"../CyFin/stock_price/stock_history_dataset/{self.set_name}/{ticker}_hist.csv"
            yf_object = yf.Ticker(ticker)
            hist = yf_object.history(start='2004-01-01', end='2022-01-01', interval='1d')
            # Normalize column names
            hist.columns = [column.lower().replace(' ', '_') for column in hist.columns]
            # Avoid creating empty datasets
            if hist.shape[0] > 0:
                hist.to_csv(path)
                print(f"{ticker} has been written.")
