from collections import Counter

def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word (case insensitive).

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    # Split the passage into words and get the first letter of each word in lowercase
    first_letters = [word[0].lower() for word in passage.split() if word]
    
    # Count occurrences of each letter
    letter_counts = Counter(first_letters)
    
    # Find the letter with the highest count
    most_common_letter, _ = letter_counts.most_common(1)[0]
    
    return most_common_letter
