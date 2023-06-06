import csv, json

from tabulate import tabulate


class DataFrame:
    def __init__(self, data=None, columns=None):
        self.data = data
        self.columns = [ column.strip() for column in columns ]

    def __repr__(self):
        return tabulate(self.data, headers=self.columns, tablefmt='psql')

    def info(self):
        if self.data is not None:
            print("Data columns (total {} columns):".format(len(self.columns)))
            for col in self.columns:
                print(col)
            print("dtypes: object")

    def display():
        return tabulate(self.data, headers=self.columns, tablefmt='html')

    def head():
        raise Exception('TODO')

    def tail():
        raise Exception('TODO')

    def iloc():
        raise Exception('TODO')

    def get_column():
        raise Exception('TODO')

    def get_mean():
        raise Exception('TODO')

    @staticmethod
    def from_csv():
        raise Exception('TODO')


    @staticmethod
    def from_json():
        raise Exception('TODO')
