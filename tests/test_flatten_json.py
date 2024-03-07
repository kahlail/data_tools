import json
# from GitHub_Profile.data_tools.flatten_json_object import flatten_json_object
from data_tools.flatten_json_object import flatten_json_object

# Arrange
test_nested_json = {
}

test_circular_reference_json = {
    "name": "Alice",
    "friends": [
        {
            "name": "Bob",
            "friends": [
                {
                    "name": "Charlie",
                    "friends": [
                        {
                            "name": "Bob",
                            "friends": [] 
                        }
                    ]
                }
            ]
        },
        {
            "name": "Charlie",
            "friends": []
        }
    ]
}

test_empty_json = {}

# This test checks to see if the function works with the expected json input
def test_flatten_json_array_happy_path():
    #Arrange
    expected_result = {
    'name': 'Alice',
    'friends_name': 'Bob',
    'friends_friends_0_name': 'Charlie',
    'friends_name': 'Charlie'
}
    # Act
    actual_result = flatten_json_object(test_json_array)
    
    # Assert
    assert actual_result == expected_result


# def test_flatten_json_object_happy_path():
#     test_data = json.dumps(test_json_array)