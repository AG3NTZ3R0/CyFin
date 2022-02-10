import matplotlib.pyplot as plt
import os
import pandas as pd
import yfinance as yf


class TickerSet:
    """Represent a set of ticker symbols."""

    def __init__(self, set_name, src_path, ticker_col, set_ticker=''):
        """Initialize attributes."""
        self.set_name = set_name
        self.set_ticker = set_ticker
        self.src_df = pd.read_csv(src_path)
        self.elements = self.src_df[ticker_col].to_list()
        self.set_element_hist_dict = dict()
        os.chdir('stock_price/sets')
        try:
            os.mkdir(self.set_name)
            os.chdir(self.set_name)
            os.mkdir('stock_hist')
            os.chdir('stock_hist')
            os.mkdir('element')
            os.mkdir('set')
            os.chdir('../')
            os.mkdir('stock_visual')
            os.chdir('stock_visual')
            os.mkdir('element')
            os.mkdir('set')
            os.chdir('../')
        except FileExistsError:
            # Compare ticker_list with saved version to ensure integrity of data (Low Priority)
            os.chdir(self.set_name)
            pass
        with open(f"{self.set_name}_tickers.txt", 'w') as ticker_file:
            ticker_file.write(' '.join(self.elements))

    def generate_hist_dataset(self):
        """Create a dataset for the set and each element in the set."""
        # Create df where close price of elements are columns and index is date (Medium Priority)
        for ticker in self.elements:
            path = f"stock_hist/element/{ticker}_hist.csv"
            yf_object = yf.Ticker(ticker)
            hist_df = yf_object.history(start='2004-01-01', end='2022-01-01', interval='1d')
            # Normalize column names
            hist_df.columns = [column.lower().replace(' ', '_') for column in hist_df.columns]
            # Avoid creating empty datasets
            if hist_df.shape[0] > 0:
                self.set_element_hist_dict[ticker] = hist_df
                hist_df.to_csv(path)

    def generate_visualization(self):
        """Create a visual for the set and each element in the set."""
        # Create visual for each element in the set (High Priority)
        plt.figure(figsize=(25, 10))
        for ticker in self.set_element_hist_dict.keys():
            plt.plot(self.set_element_hist_dict[ticker].index, self.set_element_hist_dict[ticker]['close'], label=str(ticker))
        plt.title("Price History of BUG ETF Holdings (2004 - 2022)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.margins(x=0.01)
        plt.savefig(f"stock_visual/set/{self.set_name}_visual.png")
