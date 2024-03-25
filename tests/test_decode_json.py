import pytest
from unittest.mock import patch, MagicMock
from data_tools.a_decode_json import JsonDecodingTool

class TestJsonDecodingTool:

    # Sets up a JsonDecodingTool instance that will be used for every test method in the class
    @pytest.fixture(autouse=True)
    def setup(self):
        self.dict_arrangement = JsonDecodingTool('{"key_1" : "value_1", "key_2": "value_2"}')
        self.list_arrangement = JsonDecodingTool('[{"key_1" : "value_1", "key_2": "value_2"}, {"key_3": "value_3"}]')
        
        yield
    
    # This test is checking that the function is behaving as expected. Patch decorator intercepts json.loads, and uses mock_loads instead.
    @patch('builtins.print')
    @patch('json.loads')
    def test_json_to_dict_func_behaves_as_expected(self, mock_loads, mock_print):
        # Arrange
        mock_loads.return_value = {"key_1" : "value_1", "key_2": "value_2"}

        # Act
        actual_result = self.dict_arrangement.decode_json_to_dict()

        # Assert
        mock_loads.assert_called_once_with('{"key_1" : "value_1", "key_2": "value_2"}')
        mock_print.assert_called_once_with("json object successfully converted: <class 'dict'>")
        assert actual_result == {"key_1" : "value_1", "key_2": "value_2"}

    # This test checks that func can output lists of dicts
    @patch('builtins.print')
    def test_json_to_dict_func_handles_lists(self, mock_print):
        # Arrange
        expected_result = [{"key_1" : "value_1", "key_2": "value_2"}, {"key_3": "value_3"}]

        # Act
        actual_result = self.list_arrangement.decode_json_to_dict()
        
        # Assert
        mock_print.assert_called_once_with("json object successfully converted: <class 'list'>")
        assert actual_result == expected_result

    # This test checks that the func is behaving as expected and is called with the right args, the expected amount of times.
    @patch('builtins.print')
    @patch('json.loads')
    def test_json_to_df_behaves_as_expected(self, mock_loads, mock_print):
        # Arrange
        mock_loads.return_value = {"key_1" : "value_1", "key_2": "value_2"}
        mock_data_lib = MagicMock()

        #Act
        self.dict_arrangement.decode_json_to_df(mock_data_lib)
        
        # Assert
        mock_loads.assert_called_once_with('{"key_1" : "value_1", "key_2": "value_2"}')
        mock_data_lib.read_json.assert_called_once_with({"key_1" : "value_1", "key_2": "value_2"})
        mock_print.assert_called_once_with('json object successfully converted to dataframe')

    # Tests that the correct arguments are passed, expected number of calls
    @patch('builtins.print')
    @patch('pandas.DataFrame.to_csv')
    @patch('pandas.read_json')
    def test_json_to_csv_called_with_correct_args(self, mock_pandas, mock_to_csv, mock_print):
        # Arrange
        test_fliename = 'this_is_a_test_file_name'
        mock_df = mock_pandas.return_value
        mock_df.to_csv = mock_to_csv
        
        # Act
        self.dict_arrangement.decode_json_to_csv(test_fliename)

        # Assert
        mock_pandas.assert_called_once_with('{"key_1" : "value_1", "key_2": "value_2"}')
        mock_to_csv.assert_called_once_with('this_is_a_test_file_name.csv', index=False)
        mock_print.assert_called_once_with('json object successsfully converted to csv as this_is_a_test_file_name.csv')
    
    # Tests that the correct arguments are passed, expected number of calls
    @patch('builtins.print')
    @patch('pandas.DataFrame.to_excel')
    @patch('pandas.read_json')
    def test_json_to_excel_called_with_correct_args(self, mock_pandas, mock_to_excel, mock_print):
     # Arrange
        test_filename = 'this_is_a_test_file_name'
        mock_df = mock_pandas.return_value
        mock_df.to_excel = mock_to_excel
        
        # Act
        self.dict_arrangement.decode_json_to_excel(test_filename)

        # Assert
        mock_pandas.assert_called_once_with('{"key_1" : "value_1", "key_2": "value_2"}')
        mock_to_excel.assert_called_once_with('this_is_a_test_file_name.xlsx', index=False)
        mock_print.assert_called_once_with(f'json object successsfully converted to excel sheet as {test_filename}.xlsx')
