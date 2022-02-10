from modules.ticker_set import TickerSet


def main():
    """Get stock data utilizing the ticker_set module."""
    bug_etf = TickerSet('bug_etf', '../CyFin/stock_price/bug_etf_holdings.csv', 'Ticker', set_ticker='BUG')
    bug_etf.generate_hist_dataset()
    bug_etf.generate_visualization()


if __name__ == '__main__':
    main()
