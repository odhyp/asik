from src.csv_handler import CSVHandler
from src.excel_handler import ExcelHandler
from src.generate_pdf import GeneratePDF

input_path = "data/sample.xlsx"
output_path = "data/sample.csv"
output_pdf = "data/sample.pdf"


def main():
    excel_handler = ExcelHandler()
    excel_handler.read_excel(input_path)

    csv_handler = CSVHandler()
    csv_handler.convert_to_csv(input_path, output_path)
    csv_handler.read_csv(output_path)

    generate_pdf = GeneratePDF()
    generate_pdf.create_pdf(output_pdf)


if __name__ == '__main__':
    main()
