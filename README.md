# data_tools
Re-useable modules for common data problems and tasks. 

1. flatten_json
flattens nested values in a json object so it's ready for decoding.

2. decode_json
convert a json object into a python friendly list, a pandas dataframe, a csv file or an excel file.

3. encode_json
converts a pandas dataframe, csv file or excel file into a json object.

4. is_it_a_number
checks if a column of data is numeric, and converts it.

5. is_it_text
checks if a column of data is text, and converts it.

6. time_formatter
converts a numeric value of time, into another and renames the column e.g. 60 (seconds) becomes 1 (minute)

7. date_time_formatter
converts your date time format, into another e.g. MM/DD/YYYY to DD/MM/YY

8. date_splitter
takes a date, splits it, adds each part to new columns.

9. data_concatenator
takes separate elements of a date, and concatenates them into a single value.

10. duplicate_checker
checks for and deletes duplicate entries.

