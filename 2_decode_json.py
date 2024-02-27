import json
import pandas as pd

class json_decoding_tool:
    
    def __init__(self, json_object) -> None:
        self.json_object = json_object

    # Accepts a json object and converts it into a Python List
    def decode_json_to_list_of_dicts(self) -> list:
        i = json.loads(self.json_object)
        print('json object successfully converted to a list of dictionaries')
        return i
    
    # Accepts a json object and converts it into a Pandas Data Frame
    def decode_json_to_df(self):
        i = json.loads(self.json_object)
        df = pd.json_normalize(i)
        print('json object successfully converted to dataframe (normalised)')
        return df
    
    # Converts a json object to CSV and outputs the file to the root (data_tools) directory.
    def decode_json_to_csv(self, output_csv_filename: str) -> str:
        i = json.loads(self.json_object)
        df = pd.json_normalize(i)
        df.to_csv(f'{output_csv_filename}.csv', index=False)
        return print(f'json object successsfully converted to csv as {output_csv_filename}.csv')
    
    # Converts a json object to Excel and outputs the file to the root (data_tools) directory.
    def decode_json_to_excel(self, output_excel_filename: str) -> str:
        i = json.loads(self.json_object)
        df = pd.json_normalize(i)
        df.to_excel(f'{output_excel_filename}.xlsx', index=False)
        return print(f'json object successsfully converted to excel sheet as {output_excel_filename}.xlsx')