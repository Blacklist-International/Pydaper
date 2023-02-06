class Datapulation:
    def __init__(self, data):
        self.data = data

    def Catcols(self):
        columns = self.data.columns
        return [col for col in columns if self.data[col].dtype == 'O']