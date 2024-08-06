import datetime as dt
import jinja2


def create_report(output_path):
    # 1 - Creating data for report
    data_image = "../assets/logo-bw.png"
    data_date = dt.datetime.now().strftime("%d-%m-%Y")

    # 2 - Compiled data for injecting
    context = {
        "data_image": data_image,
        "data_date": data_date
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
