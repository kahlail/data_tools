import json
import pandas as pd

class JsonDecodingTool:
    
    def __init__(self, json_object) -> None:
        self.json_object = json_object

    # Accepts a json object and converts it into a Python List
    def decode_json_to_dict(self) -> list:
        i = json.loads(self.json_object)
        print(f'json object successfully converted: {type(i)}')
        return i
    
    # Accepts a json object and converts it into a Data Frame (dependency injection so you can use either Pandas or Polars)
    def decode_json_to_df(self, data_lib):
        i = json.loads(self.json_object)
        df = data_lib.read_json(i)
        print('json object successfully converted to dataframe')
        return df
    
    # Converts a json object to CSV and outputs the file to the root (data_tools) directory.
    def decode_json_to_csv(self, output_csv_filename: str) -> str:
        df = pd.read_json(self.json_object)
        df.to_csv(f'{output_csv_filename}.csv', index=False)
        return print(f'json object successsfully converted to csv as {output_csv_filename}.csv')
    
    # Converts a json object to Excel and outputs the file to the root (data_tools) directory.
    def decode_json_to_excel(self, output_excel_filename: str) -> str:
        df = pd.read_json(self.json_object)
        df.to_excel(f'{output_excel_filename}.xlsx', index=False)
        return print(f'json object successsfully converted to excel sheet as {output_excel_filename}.xlsx')