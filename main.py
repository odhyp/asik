from src.csv_handler import CSVHandler
from src.excel_handler import ExcelHandler
from src.generate_pdf import GeneratePDF
from src.generate_report import create_report

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

    output_path = "output/sample_output.html"
    create_report(output_path=output_path)


if __name__ == '__main__':
    main()
