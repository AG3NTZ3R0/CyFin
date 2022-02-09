from modules.ticker_set import TickerSet


def main():
    """Get stock data utilizing the ticker_set module."""
    bug_etf = TickerSet('bug_etf', '../CyFin/stock_price/bug_etf_holdings.csv', 'Ticker')
    bug_etf.generate_hist_dataset()
    # Need data set to be cleaned to remove invalid symbols (not on US exchange)
    # breached_orgs = TickerSet('breached_orgs', '../breach_dataset/company_meta_dataset/company_metadata.csv', 'symbol')
    # breached_orgs.generate_hist_dataset()


if __name__ == '__main__':
    main()
