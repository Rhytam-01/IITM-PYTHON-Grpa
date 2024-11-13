def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.
    '''
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    return '-'.join(digit_words[digit] for digit in str(num))
