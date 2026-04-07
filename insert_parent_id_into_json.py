import json

import pandas as pd
from pandas import DataFrame


def read_csv(
    file_name: str,
    dtype: dict,
    dropna: list,
    encoding: str = 'utf-16',
    delimiter: str = '\t',
) -> DataFrame:
    '''
    Read a CSV file into a DataFrame with specific data types and drop rows with missing 'Object_ID' or 'Host_ID'.

    Parameters:
        file_name (str): The path to the CSV file to be read.

    Returns:
        DataFrame: A pandas DataFrame containing the CSV data.

    '''

    df = pd.read_csv(
        file_name,
        encoding=encoding,
        delimiter=delimiter,
        dtype=dtype,
    ).dropna(subset=dropna)

    return df


def read_json_file(file_name: str) -> dict:
    '''
    Read JSON data from a file and return it as a dictionary.

    Parameters:
        file_name (str): The path to the JSON file to be read.

    Returns:
        dict: A dictionary containing the JSON data read from the file.
    '''
    json_data = {}

    with open(file_name) as f:
        json_data = json.load(f)

    return json_data


def write_json_file(data: dict, filename: str) -> None:
    '''
    Write data to a JSON file with indentation.

    Parameters:
        data (dict): The dictionary containing the data to be written to the JSON file.
        filename (str): The path to the JSON file to be written.

    Returns:
        None
    '''
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
