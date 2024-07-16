import pandas as pd


class CSVHandler:
    def check_column_names(self, csv_path):
        print("Column names in the CSV file:", df.columns.tolist())

    def convert_to_csv(self, input_path, output_path):
        excel_file = pd.read_excel(input_path)
        excel_file.to_csv(output_path, index=False, header=True)

    def read_csv(self, csv_path):
        df = pd.read_csv(csv_path, sep=",", index_col=0, header=0)
        return df.to_dict(orient="records")
