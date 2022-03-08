import pandas as pd
import wxve as x


def main():
    """Get stock data."""
    api_key = 'YOUR_API_KEY'

    bug = x.Stock('BUG', api_key)
    bug.hist_df.to_csv(f"../CyFin/stock_price/sets/bug_etf/stock_hist/set/BUG_hist.csv")
    bug.hist_df.to_csv(f"../CyFin/stock_price/sets/bug_etf/stock_visual/set/BUG_visual.png")

    bug_etf_df = pd.read_csv('../CyFin/stock_price/bug_etf_holdings.csv')
    bug_etf_symbols = bug_etf_df['Ticker'].tolist()
    bug_etf = x.StockSet(bug_etf_symbols, api_key)

    for stock in bug_etf.stocks.keys():
        print(stock)
        bug_etf.stocks[stock].hist_df.to_csv(f"../CyFin/stock_price/sets/bug_etf/stock_hist/element/{stock}_hist.csv")
        bug_etf.stocks[stock].candlestick.write_image(f"../CyFin/stock_price/sets/bug_etf/stock_visual/element/{stock}_visual.png")


if __name__ == '__main__':
    main()
