import pandas as pd

input_path = "data/sample.xlsx"
output_path = "data/sample.csv"
output_json = "data/sample.json"


def read_excel(input_path):
    excel_file = pd.read_excel(input_path, index_col=0, header=0)
    print(excel_file)


def convert_to_csv(input_path, output_path):
    excel_file = pd.read_excel(input_path)
    excel_file.to_csv(output_path, index=False, header=True)


def read_csv(csv_path):
    df = pd.read_csv(csv_path, sep=",", index_col=0, header=0,
                     usecols=["nip", "nama", "norek", "gapok"])
    for item in df.itertuples():
        print(item)


def store_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df.to_json(output_path, orient="index", indent=2)


def main():
    read_excel(input_path)
    # convert_to_csv(input_path, output_path)
    # store_data(output_path, output_json)
    # read_csv(output_path)


if __name__ == '__main__':
    main()
