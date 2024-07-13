import pandas as pd


class ExcelHandler:
    def read_excel(self, input_path):
        excel_file = pd.read_excel(input_path, index_col=0, header=0)
        print(excel_file)
