def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where 
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''
    for s in strings:
        # Split the string on the hyphen
        parts = s.split('-')
        
        # Check if there are exactly two parts and they are identical and not empty
        if len(parts) != 2 or parts[0] != parts[1] or parts[0] == "":
            return False
            
    return True
