def abs_diff_between_sum_and_sum_of_squares(a: int, b: int) -> int:
    '''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    '''
    sum_ab = a + b
    sum_of_squares = a**2 + b**2
    return abs(sum_ab - sum_of_squares)


def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string, swap the parts before and after the middle three characters.
    '''
    n = len(s)
    mid = n // 2
    return s[mid+2:] + s[mid-1:mid+2] + s[:mid-1]


def interleave_lists(list1, list2, list3):
    '''
    Given three lists of the same length, interleave them together and return the interleaved list.
    '''
    return [item for triplet in zip(list1, list2, list3) for item in triplet]


def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Determine if a given integer has more than 5 unique digits.
    '''
    unique_digits = set(str(abs(num)))
    return len(unique_digits) > 5


def final_position(pos: tuple, vel: tuple, time: int) -> tuple:
    '''
    Find the final position of a point after moving with constant velocity for a given time.
    '''
    x_final = pos[0] + vel[0] * time
    y_final = pos[1] + vel[1] * time
    return (x_final, y_final)


def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove keys from a dictionary that are not present in a given list.
    '''
    keys_to_remove = [key for key in d if key not in l]
    for key in keys_to_remove:
        del d[key]
