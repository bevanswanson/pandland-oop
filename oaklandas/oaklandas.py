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

    def display(self):
        return tabulate(self.data, headers=self.columns, tablefmt='html')

    def head(self, n=5):
        raise Exception('TODO')

    def tail(self, n=5):
        raise Exception('TODO')

    def iloc(self, index):
        raise Exception('TODO')

    def get_column(self, column_name):
        raise Exception('TODO')

    def get_mean(self, column_name):
        raise Exception('TODO')

    @staticmethod
    def from_csv(path):
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            data = [ row for row in csv_reader ]
            columns = data.pop(0)

            return DataFrame(data=data, columns=columns)

    @staticmethod
    def from_json(path):
        with open(path, 'r') as file:
            json_file = json.load(file)
            columns = []
            data = []
            for line in json_file:
                cols, row = zip(*line.items())
                columns = [ col for col in cols if col not in columns ]
                data.append(list(row))

            return DataFrame(data=data, columns=columns)
