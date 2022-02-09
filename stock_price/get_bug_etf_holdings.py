from io import StringIO
import pandas as pd
import requests


def main():
    # Since the URL does not accept requests via Python it is necessary to change the header of the request
    url = "https://www.globalxetfs.com/funds/bug/?download_full_holdings=true"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/56.0.2924.76 Safari/537.36'}
    bug_etf_txt = requests.get(url, headers=headers).text
    bug_etf_df = pd.read_csv(StringIO(bug_etf_txt), sep=",", header=2)
    # Assign proper datatypes for columns
    bug_etf_df['Shares Held'] = bug_etf_df['Shares Held'].str.replace(',', '').astype(float)
    bug_etf_df['Market Value ($)'] = bug_etf_df['Market Value ($)'].str.replace(',', '').astype(float)
    # Remove  unnecessary rows (Cash & Disclaimer)
    bug_etf_df = bug_etf_df[:-2]
    # Remove ticker symbols not in US exchange
    bug_etf_df = bug_etf_df[~bug_etf_df.Ticker.str.contains(' ', regex=False)]
    # Export
    bug_etf_df.to_csv('../stock_price/bug_etf_holdings.csv')


if __name__ == '__main__':
    main()
