import pytest
from unittest.mock import patch, MagicMock
from data_tools.a_decode_json import JsonDecodingTool

class TestJsonDecodingTool:

    # Sets up a JsonDecodingTool instance that will be used for every test method in the class
    @pytest.fixture(autouse=True)
    def setup(self):
        self.arrange = JsonDecodingTool(
            {"key_1" : "value_1",
             "key_2": "value_2"}
        )

        yield

    def test_json_to_list_func_behaves_as_expected(self):
        pass

    def test_json_to_df_behaves_as_expected(self):
        pass

    def test_json_to_csv_called_with_correct_args(self):
        pass

    def test_json_to_excel_called_with_correct_args(self):
        pass