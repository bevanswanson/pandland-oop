import csv, json

import pytest

from tabulate import tabulate

from oaklandas.oaklandas import DataFrame

# oaklandas Dataframe class method
@pytest.fixture
def dataframe():
    data = [
        ['John', 30, 'New York'],
        ['Jane', 25, 'London'],
        ['Bob', 35, 'Paris']
    ]
    columns = ['Name', 'Age', 'City']
    df = DataFrame(data, columns)
    return df

def test_repr(dataframe):
    expected_output = tabulate(dataframe.data, headers=dataframe.columns, tablefmt='html')
    assert dataframe.__repr__() == expected_output

def test_head_default(dataframe):
    expected_output = tabulate(dataframe.data[:5], headers=dataframe.columns, tablefmt='html')
    assert dataframe.head() == expected_output

def test_head_n(dataframe):
    n = 2
    expected_output = tabulate(dataframe.data[:n], headers=dataframe.columns, tablefmt='html')
    assert dataframe.head(n) == expected_output

# def test_append(dataframe):
#     new_row = ['Alice', 28, 'Sydney']
#     expected_data = dataframe.data + [new_row]
#     dataframe.append(new_row)
#     assert dataframe.data == expected_data

# def test_append_with_header(dataframe):
#     new_data = [
#         ['Name', 'Age', 'City'],
#         ['Eva', 32, 'Berlin']
#     ]
#     expected_data = dataframe.data + new_data[1:]
#     dataframe.append(new_data, header=True)
#     assert dataframe.data == expected_data

def test_iloc_existing_index(dataframe):
    index = 1
    expected_row = ['Jane', 25, 'London']
    assert dataframe.iloc(index) == expected_row

def test_iloc_out_of_range_index(dataframe):
    index = 10
    expected_error = f'That row index is out of range, please select a number between 0 and {len(dataframe.data)}'
    assert dataframe.iloc(index) == expected_error

def test_get_column_existing_column(dataframe):
    column_name = 'Age'
    expected_column = [30, 25, 35]
    assert dataframe.get_column(column_name) == expected_column

def test_get_column_non_existing_column(dataframe):
    column_name = 'Salary'
    expected_error = f'The Column: {column_name} is not found in the DataFrame. It must be one of {dataframe.columns}'
    assert dataframe.get_column(column_name) == expected_error

def test_info(dataframe, capsys):
    expected_output = "Data columns (total 3 columns):\nName\nAge\nCity\ndtypes: object\n"
    dataframe.info()
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output

def test_get_mean(dataframe):
    column_name = 'Age'
    expected_mean = 30
    assert dataframe.get_mean(column_name) == expected_mean

def test_get_mean_non_numerical(dataframe):
    column_name = 'Name'
    expected_output = f"Column `{column_name}` must be of a numerical type"
    assert dataframe.get_mean(column_name) == expected_output


# df_from_csv()
@pytest.fixture
def sample_csv_file(tmp_path):
    data = [
        ['Name', 'Age', 'Salary'],
        ['John Doe', '30', '50000'],
        ['Jane Smith', '35', '60000'],
        ['Mark Johnson', '25', '40000'],
    ]
    csv_file = tmp_path / 'sample.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return csv_file

def test_df_from_csv(sample_csv_file):
    # Test the DataFrame creation from a CSV file
    df = DataFrame.from_csv(sample_csv_file)

    # Check the data and column values
    expected_data = [
        ['John Doe', '30', '50000'],
        ['Jane Smith', '35', '60000'],
        ['Mark Johnson', '25', '40000'],
    ]
    expected_columns = ['Name', 'Age', 'Salary']
    assert df.data == expected_data
    assert df.columns == expected_columns

def test_df_from_csv_header_only(tmp_path):
    # Test the case where the CSV file contains only the header row
    data = [['Name', 'Age', 'Salary']]
    csv_file = tmp_path / 'header_only.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    df = DataFrame.from_csv(csv_file)
    assert df.data == []
    assert df.columns == ['Name', 'Age', 'Salary']


# df_from_json()
@pytest.fixture
def sample_json_file(tmp_path):
    data = [
        {"Project": "Project A", "Client": "Client A", "Status": "Completed"},
        {"Project": "Project B", "Client": "Client B", "Status": "In Progress"},
        {"Project": "Project C", "Client": "Client C", "Status": "Pending"},
    ]
    json_file = tmp_path / 'sample.json'
    with open(json_file, 'w') as file:
        json.dump(data, file)
    return json_file

def test_df_from_json(sample_json_file):
    # Test the DataFrame creation from a JSON file
    df = DataFrame.from_json(sample_json_file)

    # Check the data and column values
    expected_data = [
        ["Project A", "Client A", "Completed"],
        ["Project B", "Client B", "In Progress"],
        ["Project C", "Client C", "Pending"],
    ]
    expected_columns = ["Project", "Client", "Status"]
    assert df.data == expected_data
    assert df.columns == expected_columns
