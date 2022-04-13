import pandas as pd
from datetime import datetime


def main():
    breach_dataframe = pd.read_csv('company_meta_dataset/latest_breaches.csv', skiprows=[1])
    org_dataframe = breach_dataframe['organisation']
    records_dataframe = breach_dataframe['records lost']
    date_dataframe = breach_dataframe['date']
    sector_dataframe = breach_dataframe['sector']
    method_dataframe = breach_dataframe['method']

    breach_month = []
    breach_year = []
    for _ in date_dataframe:
        date_split = _.split()
        datetime_object = datetime.strptime(date_split[0], "%b")
        month_number = datetime_object.month
        breach_month.append(month_number)
        breach_year.append(date_split[1])

    normalized_csv = pd.DataFrame({
        'company_name': org_dataframe,
        'company_sector': sector_dataframe,
        'breach_month': breach_month,
        'breach_year': breach_year,
        'breach_method': method_dataframe,
        'records_lost': records_dataframe
    })

    normalized_csv.to_csv('company_meta_dataset/normalized_breach_dataset.csv', index=True)


if __name__ == '__main__':
    main()
