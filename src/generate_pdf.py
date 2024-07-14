from fpdf import FPDF

from src.constants import (SHOW_BORDERS,
                           PAPER_SIZE,
                           PAPER_MARGINS,
                           FONT_FAMILY,
                           FONT_SIZE
                           )


class PDF(FPDF):
    def header(self):
        self.image(name="assets/logo.png",
                   x=25,
                   y=14,
                   w=30,
                   keep_aspect_ratio=True,
                   )

        self.set_font(family=FONT_FAMILY,
                      size=FONT_SIZE
                      )

        self.cell(w=30,
                  h=8,
                  new_x="RIGHT",
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
                  new_x="RIGHT",
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
                  new_x="RIGHT",
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
                   x=70,
                   y=34,
                   w=110,
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
                  new_x="RIGHT",
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
                  new_x="RIGHT",
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

    def create_page(self, output_path):
        self.add_page()

        self.set_title("Slip Gaji - ASIK")
        self.set_author("Odhy Pradhana")

        self.output(output_path)


class GeneratePDF:
    def create_pdf(self, output_path):
        pdf = PDF(orientation='P',
                  unit='mm',
                  format=PAPER_SIZE)
        pdf.set_margins(left=25.4, top=10)
        pdf.create_page(output_path)
