class DataFrame:
    def __init__(self, data=None, columns=None):
        self.data = data
        self.columns = columns

    def __repr__(self):
        return str(self.data)

    def set_data(self, data):
        self.data = data

    def set_columns(self, columns):
        self.columns = columns

    def head(self, n=5):
        if self.data is not None:
            return self.data[:n]

    def tail(self, n=5):
        if self.data is not None:
            return self.data[-n:]

    def shape(self):
        if self.data is not None:
            return len(self.data), len(self.columns)

    def info(self):
        if self.data is not None:
            print("Data columns (total {} columns):".format(len(self.columns)))
            for col in self.columns:
                print(col)
            print("dtypes: object")
