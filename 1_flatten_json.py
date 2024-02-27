from flatten_json import flatten

def flatten_json_object(json_object):
    try:
        return flatten(json_object)
    
    except AssertionError as ae:
        print(f'The json object isn\'t in the correct format:\n {ae}')
    except TypeError as te:
        print(f'Are you trying to use a Dict as the key for another Dict? \n {te}')
    except Exception as e:
        print(f'Something unexpected went wrong: {e}')