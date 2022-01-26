import pandas as pd


def main():
    breach_dataframe = pd.read_csv('Balloon Race_ Data Breaches - LATEST - breaches.csv', skiprows=[1])
    org_dataframe = breach_dataframe['organisation']
    records_dataframe = breach_dataframe['records lost']
    date_dataframe = breach_dataframe['date']
    sector_dataframe = breach_dataframe['sector']
    method_dataframe = breach_dataframe['method']

    normalized_csv = pd.DataFrame({
        'company_name': org_dataframe,
        'company_sector': sector_dataframe,
        'breach_date': date_dataframe,
        'breach_method': method_dataframe,
        'records_lost': records_dataframe
    })

    normalized_csv.to_csv('normalized_breach_dataset.csv', index=True)


if __name__ == '__main__':
    main()
