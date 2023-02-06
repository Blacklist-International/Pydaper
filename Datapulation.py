class Datapulation:
    def __init__(self, data):
        self.data = data

    def Catcols(self):
        columns = self.data.columns
        return [col for col in columns if type(data[col] == 'O')]