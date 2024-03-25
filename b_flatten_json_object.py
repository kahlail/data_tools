def flatten_json_object(nested_json):
    
    # Check that nested_json isn't empty
    if not nested_json:
        return "Error: You provided a null value."
    
    # Check that nested_json is valid json
    if isinstance(nested_json, (dict, list)):

        # Initialise a FIFO stack to store nested_json.
        stack = [((), nested_json)]
        
        # Initailise an empty dictionary to store the flattened_json.
        flattened_json = {}
        
        # While stack isn't empty, do the following:
        while stack:  
            
            path, node = stack.pop(0) # Pop the first element from the stack, and assign it to path (previous key/s) and node.

            # If the node has nested values (i.e. the node is a dictionary), do the following:
            if isinstance(node, dict): 

                for key, value in node.items(): # Loop through the key-value pairs in the dictionary.

                    # If there is another level of nesting, and the value in the node is a dictionary, do the following:
                    if isinstance(value, dict): 
                        
                        if value: # If the value is not empty
                            stack.append((path + (key,), value)) # Add a tuple of the path + current key, and value (node) to the stack.
                        else:
                            flattened_json["_".join((path + (key,)))] = '' # Else, concatente the path and current key with an underscore, and assign it to an empty string in the flattened_json dictionary.
                    
                    # Else if there is another level of nesting, and the value in the node is a list, do the following:
                    elif isinstance(value, list):

                        for i, list_element in enumerate(value):
                            stack.append((path + (key, str(i)), list_element)) # Add a tuple of the path + current key + the index of the list_element, and the list_element (node) to the stack.

                    # Else, there is no further nesting therefore do the following:
                    else:
                        flattened_json["_".join((path + (key,)))] = value # Concatente the path and current key with an underscore, and assign it to value in the flattened_json dictionary.
            
            # Else if the node has nested values (i.e. the node is a list), do the following:
            elif isinstance(node, list):
                for i, list_element in enumerate(node): # Loop through the list elements.
                    stack.append((path + (str(i),), list_element)) # Add a tuple of the path + the index of the list_element, and the list_element (node) to the stack.

            # Else the node has no nested values (is not a dictionary or a list), so do the following:
            else:
                flattened_json["_".join(path)] = node # Concatente the items in the path tuple with an underscore, and assign it to the node value in the flattened_json dictionary.

        return flattened_json 
    
    # If nested_json is not valid json, raise ValueError and provide information for user
    else:
        raise ValueError(f"This function expects a dict or list, you provided: {type(nested_json)}")