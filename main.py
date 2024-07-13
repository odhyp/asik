from src.csv_handler import CSVHandler
from src.excel_handler import ExcelHandler

input_path = "data/sample.xlsx"
output_path = "data/sample.csv"


def main():
    excel_handler = ExcelHandler()
    excel_handler.read_excel(input_path)

    csv_handler = CSVHandler()
    csv_handler.convert_to_csv(input_path, output_path)
    csv_handler.read_csv(output_path)


if __name__ == '__main__':
    main()
