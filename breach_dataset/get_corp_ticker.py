import pandas as pd
import json
from pytickersymbols import PyTickerSymbols


def main():
    stock_data = PyTickerSymbols()

    company_metadata = []

    for _ in stock_data.get_all_stocks():
        company_metadata.append(_)

    create_raw_company_data(company_metadata)

    company_raw_dataframe = pd.read_json('company_meta_dataset/company_data_raw.json')
    company_raw_dataframe.to_csv('company_meta_dataset/company_metadata.csv')


def create_raw_company_data(company_data):
    with open('company_meta_dataset/company_data_raw.json', 'w') as f:
        f.write(json.dumps(company_data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
