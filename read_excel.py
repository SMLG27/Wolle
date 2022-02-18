import pandas as pd


class ExcelData:

    def __init__(self):
        data = pd.read_excel('C:\\Users\\achos\\OneDrive\\Desktop\\Produkt_list.xlsx', index_col=[0,1])
        self.exc_data = list(data.index)
        self.produkt_list = None
        self.produkt_only_name = None

    def produkt_l(self):
        self.produkt_list = ["-".join(" ".join(e).split()) for e in self.exc_data]
        self.produkt_only_name = [(" ".join(e).split())[0] for e in self.exc_data]
        return self.produkt_list


if __name__ == '__main__':
    excel = ExcelData()
    excel.produkt_l()

