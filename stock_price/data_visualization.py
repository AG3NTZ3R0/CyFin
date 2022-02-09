import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Create a visual representation of the performance of BUG ETF holdings."""
    bug_tickers = []
    for ticker in bug_tickers:
        ticker_df = pd.read_csv(f"../stock_price/stock_history_dataset/{ticker}_hist.csv")
        print(ticker_df.columns)


if __name__ == '__main__':
    main()
