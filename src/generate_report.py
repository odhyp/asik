import datetime as dt
import jinja2


class GenerateReport:
    def format_year(date: str):
        date_object = dt.datetime.strptime(date, "%Y-%m-%d")
        year_value = date_object.year
        return year_value

    def format_month(date: str):
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

    def format_nan_value(value: str):
        """
        This function takes a value and returns it as a string.
        If the value is NaN, it returns an empty string.

        Args:
            value (str): A string of value.
        """
        if isinstance(value, float) and math.isnan(value):
            return ''
        return str(value)

    def create_report(self,
                      main_data: dict,
                      sub_data: dict,
                      config_path: str,
                      output_path: str):
        # 1 - Creating data for report
        data_image = "../assets/logo-bw.png"
        data_date = dt.datetime.now().strftime("%d-%m-%Y")

        # Title section
        title_period = main_data["tglgaji"]

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
            "employee_norek": employee_norek,

            "salary_gapok": salary_gapok,
            "salary_tunjistri": salary_tunjistri,
            "salary_tunjanak": salary_tunjanak,
            "salary_tunjstruk": salary_tunjstruk,
            "salary_tunjberas": salary_tunjberas,
            "salary_tunjpph": salary_tunjpph,
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
