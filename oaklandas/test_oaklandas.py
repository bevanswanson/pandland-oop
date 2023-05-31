import pytest

from oaklandas.oaklandas import DataFrame

@pytest.fixture
def sample_dataframe():
    data = [
        [1, 'John', 25],
        [2, 'Jane', 30],
        [3, 'Alice', 35],
        [4, 'Bob', 40]
    ]
    columns = ['ID', 'Name', 'Age']
    return DataFrame(data, columns)

def test_dataframe_repr(sample_dataframe):
    assert repr(sample_dataframe) == "[[1, 'John', 25], [2, 'Jane', 30], [3, 'Alice', 35], [4, 'Bob', 40]]"

def test_dataframe_set_data(sample_dataframe):
    new_data = [
        [5, 'Eve', 45],
        [6, 'Frank', 50]
    ]
    sample_dataframe.set_data(new_data)
    assert sample_dataframe.data == new_data

def test_dataframe_set_columns(sample_dataframe):
    new_columns = ['ID', 'Name', 'Age', 'Gender']
    sample_dataframe.set_columns(new_columns)
    assert sample_dataframe.columns == new_columns

def test_dataframe_head(sample_dataframe):
    assert sample_dataframe.head() == [[1, 'John', 25], [2, 'Jane', 30], [3, 'Alice', 35], [4, 'Bob', 40]]

def test_dataframe_tail(sample_dataframe):
    assert sample_dataframe.tail() == [[1, 'John', 25], [2, 'Jane', 30], [3, 'Alice', 35], [4, 'Bob', 40]]

def test_dataframe_shape(sample_dataframe):
    assert sample_dataframe.shape() == (4, 3)

def test_dataframe_info(sample_dataframe, capsys):
    sample_dataframe.info()
    captured = capsys.readouterr()
    expected_output = """Data columns (total 3 columns):
ID
Name
Age
dtypes: object"""
    assert captured.out.strip() == expected_output.strip()

