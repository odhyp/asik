from fpdf import FPDF


class GeneratePDF():

    class PDF(FPDF):
        def header(self):
            self.set_font("helvetica", "B", 15)
            self.cell(80)
            self.cell(30, 10, "Title", border=1, align="C")
            self.ln(20)

        def footer(self):
            self.set_y(-15)
            self.set_font("helvetica", "B", 15)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def create_pdf(self, output_path):
        pdf = self.PDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        pdf.cell(40, 10, "Hello World!")
        pdf.output(output_path)
