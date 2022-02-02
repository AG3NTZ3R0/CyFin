import pandas as pd
import yfinance as yf


def main(get_all_stock):
    start_date = '2004-01-01'
    end_date = '2022-01-01'
    country = 'United States'
    # Read CSV into pandas dataframe
    corp_dataframe = pd.read_csv('company_meta_dataset/company_metadata.csv')

    if get_all_stock:
        get_all_company_stock_price(start_date, end_date, corp_dataframe)
    else:
        get_company_stock_by_region(start_date, end_date, corp_dataframe, country)


def get_all_company_stock_price(start_date, end_date, dataframe_object):
    # Create list from Ticker column
    corp_tickers = dataframe_object['symbol'].dropna().to_list()

    for ticker in corp_tickers:
        if ' ' in ticker:
            continue
        yf_object = yf.Ticker(ticker)
        hist = yf_object.history(start=start_date, end=end_date, interval='1d')
        hist['Date'] = hist.index
        hist.to_csv(f"all_company_stock_price/{ticker}_hist.csv")
        hist.to_json(f"all_company_stock_price/{ticker}_hist.json")


def get_company_stock_by_region(start_date, end_date, dataframe_object, country):
    # Create list from Ticker column
    corp_tickers = dataframe_object.loc[(dataframe_object['country'] == country), ['symbol']]

    country = country.replace(' ', '_').lower()

    for ticker in corp_tickers:
        if ' ' in ticker:
            continue
        yf_object = yf.Ticker(ticker)
        hist = yf_object.history(start=start_date, end=end_date, interval='1d')
        hist['Date'] = hist.index
        hist.to_csv(f"{country}_company_stock_price/{ticker}_hist.csv")
        hist.to_json(f"{country}_company_stock_price/{ticker}_hist.json")


if __name__ == '__main__':
    main(get_all_stock=False)
