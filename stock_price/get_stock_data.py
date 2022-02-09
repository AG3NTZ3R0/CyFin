import os
import pandas as pd
import yfinance as yf


def main(start_date='2004-01-01', end_date='2022-01-01'):
    """Extract ticker symbols from both csv files and generate technical datasets."""
    # Read BUG CSV into pandas dataframe
    bug_full_holdings_df = pd.read_csv('./stock_price/bug_full_holdings_20220119.csv')
    # Create list from Ticker column
    bug_tickers = bug_full_holdings_df['Unnamed: 1'].to_list()
    # Delete the headers and miscellaneous data
    bug_tickers = bug_tickers[2:-2]

    # Read breach CSV into pandas dataframe
    company_metadata_df = pd.read_csv("./breach_dataset/company_meta_dataset/company_metadata.csv")
    company_metadata_tickers = company_metadata_df['symbol'].to_list()
    all_tickers = list(set(bug_tickers + company_metadata_tickers))
    all_tickers = list(map(lambda x: str(x), all_tickers))
    all_tickers = list(filter(lambda x:
                              ' ' not in x
                              and
                              '.' not in x
                              and
                              any(char.isdigit() for char in x) is not True, all_tickers))

    for ticker in all_tickers:
        path = f"./stock_price/stock_history_dataset/{ticker}_hist.csv"
        yf_object = yf.Ticker(ticker)
        hist = yf_object.history(start=start_date, end=end_date, interval='1d')
        # Normalize column names
        hist.columns = [column.lower().replace(' ', '_') for column in hist.columns]
        # Avoid the creation of empty datasets
        if hist.shape[0] > 0:
            hist.to_csv(path)


if __name__ == '__main__':
    main()
