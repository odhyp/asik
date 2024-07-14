from fpdf import FPDF

from src.constants import (SHOW_BORDERS,
                           PAPER_SIZE,
                           PAPER_MARGINS,
                           FONT_FAMILY,
                           FONT_SIZE
                           )


class GeneratePDF():

    class PDF(FPDF):
        def header(self):
            self.image(name="assets/logo.png",
                       x=10,
                       y=10,
                       w=30,
                       keep_aspect_ratio=True,
                       )

            self.set_font(family=FONT_FAMILY,
                          size=FONT_SIZE
                          )

            self.cell(w=30,
                      h=8,
                      new_x="LMARGIN",
                      border=SHOW_BORDERS
                      )

            self.cell(w=0,
                      h=8,
                      text="PEMERINTAH DAERAH DAERAH ISTIMEWA YOGYAKARTA",
                      align="C",
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.cell(w=30,
                      h=8,
                      new_x="LMARGIN",
                      border=SHOW_BORDERS
                      )

            self.cell(w=0,
                      h=8,
                      text="BADAN PENGELOLA KEUANGAN DAN ASET",
                      align="C",
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.cell(w=30,
                      h=8,
                      new_x="LMARGIN",
                      border=SHOW_BORDERS
                      )

            self.cell(w=0,
                      h=8,
                      text="KPPD DIY DI KABUPATEN BANTUL",
                      align="C",
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.image(name="assets/placeholder.png",
                       x=40,
                       y=34,
                       w=160,
                       h=8,
                       )

            self.cell(w=0,
                      h=8,
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.cell(w=30,
                      h=8,
                      new_x="LMARGIN",
                      border=SHOW_BORDERS
                      )

            self.cell(w=0,
                      h=8,
                      text="Alamat: Jalan Urip Sumoharjo Telepone/Fax: 0274-367483",
                      align="C",
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.cell(w=30,
                      h=8,
                      new_x="LMARGIN",
                      border=SHOW_BORDERS
                      )

            self.cell(w=0,
                      h=8,
                      text="BANTUL 55711",
                      align="C",
                      new_x="LMARGIN",
                      new_y="NEXT",
                      border=SHOW_BORDERS
                      )

            self.ln(20)

        def footer(self):
            self.set_y(-15)
            self.set_font("helvetica", "B", size=16)
            self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def create_pdf(self, output_path):
        pdf = self.PDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=16)
        pdf.cell(40, 10, "Hello World!")
        pdf.output(output_path)
