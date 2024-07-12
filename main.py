import pandas as pd

input_path = "data/sample.xlsx"
output_path = "data/sample.csv"


def convert_to_csv(input_path, output_path):
    excel_file = pd.read_excel(input_path)
    excel_file.to_csv(output_path, index=False, header=True)


def read_csv(csv_path):
    df = pd.read_csv(csv_path, sep=",", index_col=0, header=0,
                     usecols=["nip", "nama", "norek", "gapok"])
    for item in df.itertuples():
        print(item)


def main():
    convert_to_csv(input_path, output_path)
    read_csv(output_path)


if __name__ == '__main__':
    main()
