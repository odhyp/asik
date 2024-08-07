import pandas as pd


class CSVHandler:
    """
    A class to handle CSV file operations.
    """
    def convert_to_csv(self, input_path: str, output_path: str):
        """
        Converts an Excel file to a CSV file.

        Args:
            input_path (str): The path to the input Excel file.
            output_path (str): The path to the output CSV file.
        """
        excel_file = pd.read_excel(input_path)
        excel_file.to_csv(output_path, index=False, header=True)

    def read_csv(self, csv_path: str) -> list:
        """
        Reads a CSV file and returns its contents as a list of dictionaries.

        Args:
            csv_path (str): The path to the CSV file.

        Returns:
            list: A list of dictionaries representing the CSV data.
        """
        df = pd.read_csv(csv_path, sep=",", index_col=0, header=0)
        return df.to_dict(orient="records")
