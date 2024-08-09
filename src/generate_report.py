import datetime as dt
import jinja2
import math
from terbilang import Terbilang


class GenerateReport:
    def is_float(self, value: float):
        return isinstance(value, float)

    def is_nan(self, value: float):
        return math.isnan(value)

    def format_number(self, value: int):
        return f"{value:,}".replace(',', '.')

    def format_year(self, date: str):
        date_object = dt.datetime.strptime(date, "%Y-%m-%d")
        year_value = date_object.year
        return year_value

    def format_month(self, date: str):
        date_object = dt.datetime.strptime(date, "%Y-%m-%d")
        month_value = date_object.month
        month_id = {
            1: "Januari",
            2: "Februari",
            3: "Maret",
            4: "April",
            5: "Mei",
            6: "Juni",
            7: "Juli",
            8: "Agustus",
            9: "September",
            10: "Oktober",
            11: "November",
            12: "Desember"
        }
        return month_id[month_value]

    def format_date(self, date: str):
        date_object = dt.datetime.strptime(date, "%Y-%m-%d")
        date_value = date_object.day
        return str(date_value).zfill(2)

    def format_nan_value(self, value: str):
        """
        This function takes a value and returns it as a string.
        If the value is NaN, it returns an empty string.

        Args:
            value (str): A string of value.
        """
        if self.is_float(value) and self.is_nan(value):
            return ''
        return str(value)

    def format_terbilang(self, value: int):
        t = Terbilang()
        result = t.parse(value).getresult()
        return f"{result} rupiah".title()

    def format_glrbelakang(self, glrbelakang: str):
        if self.is_float(glrbelakang) and self.is_nan(glrbelakang):
            return ''
        return str(f", {glrbelakang}")

    def format_tjumum(self, tjeselon: int, tjumum: int):
        if tjeselon != 0:
            return tjeselon
        else:
            return tjumum

    def format_gol(self, gol: str):
        golongan = {
            "1A": "I/a",
            "1B": "I/b",
            "1C": "I/c",
            "1D": "I/d",
            "2A": "II/a",
            "2B": "II/b",
            "2C": "II/c",
            "2D": "II/d",
            "3A": "III/a",
            "3B": "III/b",
            "3C": "III/c",
            "3D": "III/d",
            "4A": "IV/a",
            "4B": "IV/b",
            "4C": "IV/c",
            "4D": "IV/d",
            "4E": "IV/e",
        }
        pangkat = {
            "1A": "Juru Muda",
            "1B": "Juru Muda Tk. I",
            "1C": "Juru",
            "1D": "Juru Tk. I",
            "2A": "Pengatur Muda",
            "2B": "Pengatur Muda Tk. I",
            "2C": "Pengatur",
            "2D": "Pengatur Tk. I",
            "3A": "Penata Muda",
            "3B": "Penata Muda Tk. I",
            "3C": "Penata",
            "3D": "Penata Tk. I",
            "4A": "Pembina",
            "4B": "Pembina Tk. I",
            "4C": "Pembina Utama Muda",
            "4D": "Pembina Utama Madya",
            "4E": "Pembina Utama",
        }
        return f"{pangkat[gol]}, {golongan[gol]}"

    def create_report(self,
                      main_data: dict,
                      sub_data: dict,
                      config: dict,
                      output_path: str):
        # 1 - Creating data for report
        data_image = "../assets/logo-bw.png"

        # Title section
        data_year = self.format_year(main_data["tglgaji"])
        data_month = self.format_month(main_data["tglgaji"])
        data_date = self.format_date(main_data["tglgaji"])
        title_period = f"{data_month} {data_year}"

        # Employee section
        data_glrdepan = self.format_nan_value(main_data["glrdepan"])
        data_glrbelakang = self.format_glrbelakang(main_data["glrbelakang"])
        employee_name = f"{data_glrdepan}{main_data["nama"]}{data_glrbelakang}"
        employee_nip = main_data["nip"]
        employee_gol = self.format_gol(main_data["kdpangkat"])

        # Earnings section
        salary_gapok = self.format_number(main_data["gapok"])
        salary_tjistri = self.format_number(main_data["tjistri"])
        salary_tjanak = self.format_number(main_data["tjanak"])
        salary_tjumum = self.format_number(
            self.format_tjumum(main_data["tjeselon"], main_data["tjumum"]))
        salary_tjberas = self.format_number(main_data["tjberas"])
        salary_tjpph = self.format_number(main_data["tjpajak"])
        salary_pembulatan = self.format_number(main_data["tbulat"])

        data_jumlahkotor = main_data["kotor"]
        salary_jumlahkotor = self.format_number(data_jumlahkotor)

        # Deductions section
        salary_iwp8 = self.format_number(main_data["piwp8"])
        salary_iwp1 = self.format_number(main_data["piwp1"])
        salary_pph = self.format_number(main_data["ppajak"])

        salary_bpd = self.format_number(sub_data["bankbpd"])
        salary_korpri = self.format_number(sub_data["korpri"])
        salary_dw = self.format_number(sub_data["dw"])
        salary_zakat = self.format_number(sub_data["bazis"])
        salary_pelita = self.format_number(sub_data["pelita"])
        salary_beras = self.format_number(sub_data["beras"])
        salary_lain = self.format_number(sub_data["lain"])

        data_potwajib = main_data["potongan"]
        data_potbend = sub_data["jumlah"]
        data_jumlahpot = data_potwajib + data_potbend
        salary_jumlahpot = self.format_number(data_jumlahpot)

        # Final section
        data_bersih = data_jumlahkotor - data_jumlahpot
        final_bersih = self.format_number(data_bersih)
        final_terbilang = self.format_terbilang(data_bersih)

        # Signature section
        signature_place = config["tempat"]
        signature_date = f"{data_date} {data_month} {data_year}"
        signature_name = config["nama"]
        signature_nip = config["nip"]

        # 2 - Compiled data for injecting
        context = {
            "header_logo": "../assets/logo-bw.png",
            "header_aksara": "../assets/aksara.png",
            "signature_image": "../assets/signature.png",
            "signature_stamp": "../assets/stamp.png",

            "header_pemda": "Pemerintah Daerah Daerah Istimewa Yogyakarta",
            "header_opd": "Badan Pengelola Keuangan dan Aset",
            "header_upt": "KPPD DIY Di Kabupaten Bantul",
            "header_address": "Jalan Urip Sumoharjo, Bantul",
            "header_telp": "0274-367483",
            "header_kodepos": "55711",

            "title_period": title_period,

            "employee_name": employee_name,
            "employee_nip": employee_nip,
            "employee_gol": employee_gol,

            "salary_gapok": salary_gapok,
            "salary_tjistri": salary_tjistri,
            "salary_tjanak": salary_tjanak,
            "salary_tjumum": salary_tjumum,
            "salary_tjberas": salary_tjberas,
            "salary_tjpph": salary_tjpph,
            "salary_pembulatan": salary_pembulatan,
            "salary_jumlahkotor": salary_jumlahkotor,

            "salary_iwp8": salary_iwp8,
            "salary_iwp1": salary_iwp1,
            "salary_pph": salary_pph,

            "salary_bpd": salary_bpd,
            "salary_korpri": salary_korpri,
            "salary_dw": salary_dw,
            "salary_zakat": salary_zakat,
            "salary_pelita": salary_pelita,
            "salary_beras": salary_beras,
            "salary_lain": salary_lain,
            "salary_jumlahpot": salary_jumlahpot,

            "final_bersih": final_bersih,
            "final_terbilang": final_terbilang,

            "signature_place": signature_place,
            "signature_date": signature_date,
            "signature_name": signature_name,
            "signature_nip": signature_nip,
        }

        # 3 - Create jinja template object from file
        template = jinja2.Environment(
            loader=jinja2.FileSystemLoader("templates/"),
            autoescape=jinja2.select_autoescape
        ).get_template("slip.html")

        # 4 - Render data in jinja template
        slip_text = template.render(context)

        # 5 - Save generated text as a HTML file
        with open(output_path, mode="w") as f:
            f.write(slip_text)
