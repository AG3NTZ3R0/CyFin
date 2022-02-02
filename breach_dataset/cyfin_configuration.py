import pandas as pd


class CyFin:
    def __init__(self):
        self.__df = pd.read_csv('company_meta_dataset/company_metadata.csv')

    def region_dir_creation(self):
        print(self.__df['country'])


def main():
    cf = CyFin()
    cf.region_dir_creation()


if __name__ == '__main__':
    main()
