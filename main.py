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
    df = pd.read_csv(csv_path, sep=",", index_col=0, header=0)

    # Check column names
    # print("Column names in the CSV file:", df.columns.tolist())

    for index, row in df.iterrows():
        value_nip = row['nip']
        value_nama = row['nama']
        value_gapok = row['gapok']

        print(f"NIP : {value_nip}")
        print(f"Nama : {value_nama}")
        print(f"Gapok : {value_gapok}")
        print("\n")


def main():
    # read_excel(input_path)
    # convert_to_csv(input_path, output_path)
    read_csv(output_path)


if __name__ == '__main__':
    main()
