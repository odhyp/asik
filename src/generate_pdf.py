from fpdf import FPDF


class GeneratePDF:
    def create_pdf(self, output_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        pdf.cell(40, 10, "Hello World!")
        pdf.output(output_path)
