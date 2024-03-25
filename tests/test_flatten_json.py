import pytest
from data_tools.b_flatten_json_object import flatten_json_object

# This test checks that the function works with the expected json input
def test_will_flatten_nested_json():
    #Arrange
    nested_json = {
  "person": {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "123 Main St",
      "city": "Anytown",
      "state": "Anystate",
      "postal_code": "12345"
    },
  },
  "company": {
    "name": "Acme Corporation",
    "industry": "Technology",
    "employees": [
      {
        "name": "Jane Smith",
        "position": "Software Engineer"
      },
      {
        "name": "Bob Johnson",
        "position": "Project Manager"
      }
    ]
  }
}
    expected_result = {
    "person_name": "John Doe",
    "person_age": 30,
    "person_address_street": "123 Main St",
    "person_address_city": "Anytown",
    "person_address_state": "Anystate",
    "person_address_postal_code": "12345",
    "company_name": "Acme Corporation",
    "company_industry": "Technology",
    "company_employees_0_name": "Jane Smith",
    "company_employees_0_position": "Software Engineer",
    "company_employees_1_name": "Bob Johnson",
    "company_employees_1_position": "Project Manager"
}
    # Act
    actual_result = flatten_json_object(nested_json)
    
    # Assert
    assert actual_result == expected_result


# This test checks the function can handle circular references correctly
def test_will_flatten_json_with_circular_references():
    # Arrange
    circular_reference_json = {
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
    expected_result = {
        'name': 'Alice', 
        'friends_0_name': 'Bob', 
        'friends_1_name': 'Charlie', 
        'friends_0_friends_0_name': 'Charlie', 
        'friends_0_friends_0_friends_0_name': 'Bob'
}
    # Act
    actual_result = flatten_json_object(circular_reference_json)

    # Assert
    assert actual_result == expected_result


# This test checks that the function can handle an empty json
def test_can_handle_empty_input():
    # Arrange
    empty_json = {}
    expected_result = "Error: You provided a null value."

    # Act
    actual_result = flatten_json_object(empty_json)

    # Assert
    assert actual_result == expected_result
    
# This test checks that the function can handle an unexpected numeric input
def test_can_handle_unexpected_input_numeric():
    # Arrange
    not_json_is_numeric = 23940
    expected_message = "This function expects a dict or list, you provided: <class 'int'>"

    # Act
    with pytest.raises(ValueError, match=expected_message):
        flatten_json_object(not_json_is_numeric)
    

# This test checks that the function can handle an unexpected string input
def test_can_handle_unexpected_input_string():
    # Arrange
    not_json_is_str = "Hello, world!"
    expected_message = "This function expects a dict or list, you provided: <class 'str'>"

    # Act
    with pytest.raises(ValueError, match=expected_message):
        flatten_json_object(not_json_is_str)
    

# This test checks that the function can handle an unexpected tuple input
def test_can_handle_unexpected_input_tuple():
    # Arrange
    not_json_is_tuple = ("Hello", 3, "is my lucky number!")
    expected_message = "This function expects a dict or list, you provided: <class 'tuple'>"
    
    # Act
    with pytest.raises(ValueError, match=expected_message):
        flatten_json_object(not_json_is_tuple)
   