import pandas as pd
import yfinance as yf


def main(start_date='2004-01-01', end_date='2022-01-01'):
    """Extract ticker symbols from BUG csv file and gather price history"""
    # Read CSV into pandas dataframe
    bug_full_holdings = pd.read_csv('bug_full_holdings_20220119.csv')
    # Create list from Ticker column
    bug_tickers = bug_full_holdings['Unnamed: 1'].to_list()
    # Delete the headers and miscellaneous data
    bug_tickers = bug_tickers[2:-2]

    for ticker in bug_tickers:
        if ' ' in ticker:
            continue
        yf_object = yf.Ticker(ticker)
        hist = yf_object.history(start=start_date, end=end_date, interval='1d')
        hist['Date'] = hist.index
        hist.to_csv(f"stock_price_ds/{ticker}_hist.csv")


if __name__ == '__main__':
    main()
