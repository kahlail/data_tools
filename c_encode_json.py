import json
import polars as pl

class JsonEncodingTool:
    
    def __init__(self, some_data) -> None:
        self.some_data = some_data

    # Accepts a list of dicts and converts it to a json object
    def encode_list_of_dicts_to_json(self):
        i = json.loads(self.some_data)
        print('List of dictionaries has been successfully converted to a json object')
        return i

    # Accepts a Polars Data Frame and converts it to a json object
    def encode_polars_df_to_json(self):
        self
        pass
    
    # Accepts a .csv file and converts it to a json object
    def encode_json_to_csv(self):
        pass
    
    # Accepts an Excel file and converts it to a json object
    def encode_json_to_excel(self):
        pass