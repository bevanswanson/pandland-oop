import csv, json

from tabulate import tabulate


class DataFrame:
    def __init__(self, data=None, columns=None):
        self.data = data
        self.columns = [ column.strip() for column in columns ]

    def __repr__(self):
        return tabulate(self.data, headers=self.columns, tablefmt='html')

    def info(self):
        if self.data is not None:
            print("Data columns (total {} columns):".format(len(self.columns)))
            for col in self.columns:
                print(col)
            print("dtypes: object")

    def head(self, n=5):
        return tabulate(self.data[:n], headers=self.columns, tablefmt='html')

    def tail(self, n=5):
        return tabulate(self.data[:n], headers=self.columns, tablefmt='html')

    # def append(self, data, header=None):
    #     if header:
    #         data = [ row for row in data ]
    #         columns = data.pop(0)
    #         self.data.append(data)
    #     else:
    #         self.data.append(data)

    def iloc(self, index):
        try:
            return self.data[index]
        except IndexError:
            return f'That row index is out of range, please select a number between 0 and {len(self.data)}'

    def get_column(self, column_name):
        try:
            col_index = self.columns.index(column_name)
            return [ row[col_index] for row in self.data ]
        except ValueError:
            return f'The Column: {column_name} is not found in the DataFrame. It must be one of {self.columns}'

    def get_mean(self, column_name):
        data = self.get_column(column_name)
        try:
            return sum([ int(num) for num in data ]) / len(data)
        except ValueError:
            return f'Column `{column_name}` must be of a numerical type'

def df_from_csv(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        data = [ row for row in csv_reader ]
        columns = data.pop(0)

        return DataFrame(data=data, columns=columns)

def df_from_json(path):
    with open(path, 'r') as file:
        json_file = json.load(file)
        columns = []
        data = []
        for line in json_file:
            cols, row = zip(*line.items())
            columns = [ col for col in cols if col not in columns ]
            data.append(list(row))

        return DataFrame(data=data, columns=columns)