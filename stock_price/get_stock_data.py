import os
import pandas as pd
import yfinance as yf


# Two text files containing the clean ticker symbols of BUG ETF and breached organizations


def clean_tickers(tickers):
    """Remove invalid ticker symbols from list."""
    tickers = list(set(tickers))
    tickers = list(map(lambda x: str(x), tickers))
    tickers = list(filter(lambda x:
                          ' ' not in x
                          and
                          '.' not in x
                          and
                          any(char.isdigit() for char in x) is not True, tickers))
    return tickers


def create_datasets(tickers, dir_path, start_date='2004-01-01', end_date='2022-01-01'):
    """Create dataset for each ticker symbol in list."""
    for ticker in tickers:
        path = f"./{dir_path}/{ticker}_hist.csv"
        yf_object = yf.Ticker(ticker)
        hist = yf_object.history(start=start_date, end=end_date, interval='1d')
        # Normalize column names
        hist.columns = [column.lower().replace(' ', '_') for column in hist.columns]
        # Avoid the creation of empty datasets
        if hist.shape[0] > 0:
            hist.to_csv(path)
            print(f"{ticker} has been written.")


def main():
    """Extract ticker symbols from both csv files and generate technical datasets."""
    # Read BUG CSV into pandas dataframe
    bug_full_holdings_df = pd.read_csv('./stock_price/bug_full_holdings_20220119.csv')
    # Create list from Ticker column
    bug_tickers = bug_full_holdings_df['Unnamed: 1'].to_list()
    # Delete the headers and miscellaneous data
    bug_tickers = bug_tickers[2:-2]
    bug_tickers = clean_tickers(bug_tickers)
    # Write list to text file
    with open('./stock_price/ticker_lists/bug_etf_tickers.txt', 'w') as bug_ticker_file:
        bug_ticker_file.write(' '.join(bug_tickers))
    # Create datasets
    create_datasets(bug_tickers, 'stock_price/stock_history_dataset/bug_etf')

    # Read breach CSV into pandas dataframe
    breached_org_df = pd.read_csv("./breach_dataset/company_meta_dataset/company_metadata.csv")
    # Create list from Ticker column
    breached_org_tickers = breached_org_df['symbol'].to_list()
    # Delete the headers and miscellaneous data
    breached_org_tickers = clean_tickers(breached_org_tickers)
    # Write list to text file
    with open('./stock_price/ticker_lists/breached_org_tickers.txt', 'w') as breached_org_ticker_file:
        breached_org_ticker_file.write(' '.join(breached_org_tickers))
    # Create datasets
    create_datasets(breached_org_tickers, 'stock_price/stock_history_dataset/breached_orgs')


if __name__ == '__main__':
    main()
