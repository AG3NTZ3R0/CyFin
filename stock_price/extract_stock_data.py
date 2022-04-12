import pandas as pd
import yh_finance as yhf


def main():
    """Get stock data using wxve."""
    api_key = 'YOUR_API_KEY'

    bug_etf_df = pd.read_csv('../CyFin/stock_price/bug_etf_holdings.csv')
    bug_etf_symbols = bug_etf_df['Ticker'].tolist()

    for stock in bug_etf_symbols:
        print(stock)
        json_resp_month = yhf.get_chart(interval='1mo',
                                        symbol=stock,
                                        time_range='10y',
                                        region='US',
                                        include_pre_post='false',
                                        use_yahoo_id='true',
                                        include_adj_close='true',
                                        events='div',
                                        api_key=api_key)

        month_data = pd.DataFrame()
        month_data['date'] = pd.to_datetime(json_resp_month['chart']['result'][0]['timestamp'], unit='s').date
        month_data['month'] = pd.to_datetime(json_resp_month['chart']['result'][0]['timestamp'], unit='s').month
        month_data['year'] = pd.to_datetime(json_resp_month['chart']['result'][0]['timestamp'], unit='s').year
        month_data['adjclose'] = json_resp_month['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
        month_data.to_csv(f"../CyFin/stock_price/sets/bug_etf/stock_hist/element/{stock}_hist.csv")


if __name__ == '__main__':
    main()
