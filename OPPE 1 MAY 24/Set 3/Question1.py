def square_and_clip(x: int, threshold: int) -> int:
    '''
    Square the given integer and clip the result to threshold.
    '''
    squared = x * x
    return min(squared, threshold)


def lowercase_first_half_and_uppercase_second_half(s: str) -> str:
    '''
    Given an even-length string, make the first half lowercase and the second half uppercase.
    '''
    half = len(s) // 2
    return s[:half].lower() + s[half:].upper()


def add_the_middle_element_to_both_ends(l: list) -> None:
    '''
    Given an odd-length list, insert the middle element to both ends.
    '''
    middle_index = len(l) // 2
    middle_element = l[middle_index]
    l.insert(0, middle_element)
    l.append(middle_element)


def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Count unique digits common in both numbers.
    '''
    set1 = set(str(n1))
    set2 = set(str(n2))
    return len(set1 & set2)


def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Calculate Manhattan distance from point a to point c via point b.
    '''
    distance_a_to_b = abs(a[0] - b[0]) + abs(a[1] - b[1])
    distance_b_to_c = abs(b[0] - c[0]) + abs(b[1] - c[1])
    return distance_a_to_b + distance_b_to_c


def create_indexed_dict(names: list) -> dict:
    '''
    Create a dictionary with indices as keys and names as values.
    '''
    return {i: name for i, name in enumerate(names)}
