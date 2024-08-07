import datetime as dt
import jinja2


def create_report(output_path):
    # 1 - Creating data for report
    data_image = "../assets/logo-bw.png"
    data_date = dt.datetime.now().strftime("%d-%m-%Y")

    # 2 - Compiled data for injecting
    context = {
        "header_pemda": "Pemerintah Daerah Daerah Istimewa Yogyakarta",
        "header_opd": "Badan Pengelola Keuangan dan Aset",
        "header_upt": "KPPD DIY Di Kabupaten Bantul",
        "header_address": "Jalan Urip Sumoharjo, Bantul",
        "header_telp": "0274-367483",
        "header_kodepos": "55711",

        "title_period": "Agustus 2024",

        "employee_name": employee_name,
        "employee_nip": employee_nip,
        "employee_gol": employee_gol,
        "employee_status": employee_status,

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

        "signature_place": "Bantul",
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
    report_text = template.render(context)

    # 5 - Save generated text as a HTML file
    with open(output_path, mode="w") as f:
        f.write(report_text)
