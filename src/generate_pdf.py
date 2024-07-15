from fpdf import FPDF

SHOW_BORDERS = False
PAPER_SIZE = (215, 330)  # Page size in mm
PAPER_MARGINS = 25.4  # Page margins in mm

FONT_FAMILY = "times"
FONT_SIZE = 12


class PDF(FPDF):
    def header(self):
        self.image(name="assets/logo.png",
                   x=28,
                   y=10,
                   w=28,
                   keep_aspect_ratio=True,
                   )

        self.set_font(family=FONT_FAMILY,
                      size=FONT_SIZE
                      )

        self.cell(w=30,
                  h=6,
                  new_x="RIGHT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  text="PEMERINTAH DAERAH DAERAH ISTIMEWA YOGYAKARTA",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.set_font(family=FONT_FAMILY,
                      size=14
                      )

        self.cell(w=30,
                  h=6,
                  new_x="RIGHT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  text="BADAN PENGELOLA KEUANGAN DAN ASET",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=30,
                  h=6,
                  new_x="RIGHT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  text="KPPD DIY DI KABUPATEN BANTUL",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=8,
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.image(name="assets/placeholder.png",
                   x=70,
                   y=28,
                   w=110,
                   h=8,
                   )

        self.set_font(family=FONT_FAMILY,
                      size=10
                      )

        self.cell(w=30,
                  h=6,
                  new_x="RIGHT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  text="Alamat: Jalan Urip Sumoharjo Telepone/Fax: 0274-367483",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=30,
                  h=6,
                  new_x="RIGHT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  text="BANTUL 55711",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS
                  )

        self.cell(w=0,
                  h=6,
                  border="T"
                  )

        self.ln(10)

    def footer(self):
        self.set_y(-15)

        self.set_font(family=FONT_FAMILY,
                      size=FONT_SIZE,
                      style="I"
                      )

        self.set_text_color(r=119,
                            g=119,
                            b=119)

        self.cell(w=0,
                  h=8,
                  text=f"This page is generated using ASIK 2.0",
                  align="C",
                  link="https://github.com/odhyp/asik",
                  border=SHOW_BORDERS
                  )

    def section_title(self):
        self.set_font(family=FONT_FAMILY,
                      size=14,
                      style="B"
                      )

        self.cell(w=0,
                  h=6,
                  text="SLIP GAJI",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS)

        self.set_font(family=FONT_FAMILY,
                      size=FONT_SIZE,
                      )

        self.cell(w=0,
                  h=6,
                  text="Bulan: Juli 2024",
                  align="C",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS)

        self.ln(10)

    def section_main(self):
        self.cell(w=30,
                  h=8,
                  text="NIP",
                  new_x="RIGHT",
                  border=SHOW_BORDERS)

        self.cell(w=10,
                  h=8,
                  text=":",
                  align="C",
                  new_x="RIGHT",
                  border=SHOW_BORDERS)

        self.cell(w=0,
                  h=8,
                  text="199904192021021002",
                  new_x="LMARGIN",
                  new_y="NEXT",
                  border=SHOW_BORDERS)

    def create_page(self, output_path):
        self.add_page()

        self.set_title("Slip Gaji - ASIK")
        self.set_author("Odhy Pradhana")

        self.section_title()
        self.section_main()

        self.output(output_path)


class GeneratePDF:
    def create_pdf(self, output_path):
        pdf = PDF(orientation='P',
                  unit='mm',
                  format=PAPER_SIZE)
        pdf.set_margins(left=25.4, top=10)
        pdf.create_page(output_path)
