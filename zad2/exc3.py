import pandas as pd


class DataFile(object):

    def __init__(self, filename='undef'):
        self.matrix = []
        self.data_frame = pd.read_csv(filename, sep=';')
        self.columns = list(self.data_frame.columns.values)

    def info(self):
        first_column = self.columns.pop(0)
        print('Name: ', end='')
        print(self.data_frame[first_column].values, sep='   ')

        for column in self.columns:
            tmp = []
            tmp.append(self.avg(0, column))
            tmp.append(self.max(0, column))
            tmp.append(self.min(0, column))
            print(column + ' : ', end='')
            print(tmp, sep='   ')

    def avg(self, colnum=0, colname=''):
        """ The column name or colnum can be provided alternatively
        """
        if colname != '':
            values = self.data_frame[colname].values
        else:
            values = self.data_frame.iloc[:, [colnum]].values

        return round(float(sum(values) / len(values)), 2)

    def min(self, colnum=0, colname=''):
        if colname != '':
            values = self.data_frame[colname].values
        else:
            values = self.data_frame.iloc[:, [colnum]].values

        return float(min(values))

    def max(self, colnum=0, colname=''):
        if colname != '':
            values = self.data_frame[colname].values
        else:
            values = self.data_frame.iloc[:, [colnum]].values

        return float(max(values))


df = DataFile('test_file.csv')
df.info()
