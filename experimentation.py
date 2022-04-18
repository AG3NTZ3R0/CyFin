import numpy as np
import pandas as pd

from stock_price.extract_stock_data import get_bug_holdings


def main():
    breach_df = pd.read_csv('../CyFin/breach_dataset/company_meta_dataset/normalized_breach_dataset.csv')

    breach_df['records_lost'] = breach_df.records_lost.str.split(',').str.join('').astype(int)
    breach_df = breach_df.rename(columns={'breach_month': 'month', 'breach_year': 'year'})

    breach_df = breach_df.groupby(['month', 'year'])['records_lost'].sum().to_frame()

    analysis_df = pd.DataFrame()
    bug_etf_symbols = get_bug_holdings()
    for stock in bug_etf_symbols:
        stock_df = pd.read_csv(f"../CyFin/stock_price/sets/bug_etf/stock_hist/element/{stock}_hist.csv")
        stock_df = stock_df.drop(['Unnamed: 0', 'date', 'adjclose'], axis=1)
        stock_df = stock_df.rename(columns={'adjclose': f"{stock}_adjclose", 'pct_change': f"{stock}_pct_change"})
        breach_df = pd.merge(breach_df, stock_df, on=['month', 'year'], how='left')

    breach_df.to_csv('breach_bug_df.csv')


if __name__ == '__main__':
    main()
