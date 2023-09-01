from typing import Dict


def longest_substring_without_repeating_characters_3(s: str) -> int:  # PASSED
    pointer = 0
    longest_string = 0
    for i in range(len(s)):
        used_chars = []
        for j in range(i, len(s)):
            char = s[j]

            # if i == 0 and j == 1:
            #     longest_string = 1

            if char in used_chars:
                break

            else:
                if j - (i - 1) > longest_string:
                    longest_string = j - (i - 1)
                    print(i, j, longest_string)

            used_chars.append(char)

    return longest_string


# print(longest_substring_without_repeating_characters_3('abcdefabbdeufhgkjo'))


def valid_parenthesis_20(s: str) -> bool:  # PASSED
    # The parenthesis must close within the bracket they were opened
    # i.e. ([]) == ok, ([)] == bad

    sets = {')': '(', ']': '[', '}': '{'}
    # par = ['(', ')']
    # box = ['[', ']']
    # curl = ['{', '}']
    opens = ['(', '{', '[']
    # closes = [')', '}', ']']

    opened = []

    for char in s:
        if char in opens:
            opened.append(char)

        elif len(opened) <= 0:
            return False

        elif opened.pop() != sets[char]:
            return False

    return len(opened) == 0

    """
    count_open = {'(': 0, '{': 0,  '[': 0}
    count_closed = {')': 0, '}': 0, ']': 0}

    open_list = list(count_open.keys())
    closed_list = list(count_closed.keys())

    for char in s:
        # print(type(open_list), open_list)
        if char in closed_list:
            count_closed[char] += 1
            # if count_open[open_list[closed_list.index(char)]] < count_closed[char]:
            #     return False

        else:
            count_open[char] += 1

    for index, value in enumerate(count_open):
        # print(index, value)
        if count_open[value] != count_closed[closed_list[index]]:
            return False

    return True
    """


# print(valid_parenthesis_20('(){}[]'))
# print(valid_parenthesis_20('[[[]]{]}({[)]'))


def median_of_two_sorted_arrays_4(nums1: list[int], nums2: list[int]) -> float:  # PASSED (though this seems to be O(n + m) when it should be O(log(n + m)).)
    import math
    # median = nums1[len(nums1) / 2]

    i = 0
    j = 0
    nums3 = []

    while i < len(nums1) or j < len(nums2):
        if i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1 if i < len(nums1) else 0
        elif j < len(nums2):
            nums3.append(nums2[j])
            j += 1 if j < len(nums2) else 0
        else:
            nums3.append(nums1[i])
            i += 1

    # print(i, j, nums3)
    midpoint = len(nums3) / 2.0
    # if len(nums3) % 2 == 0:
    print(midpoint, math.floor(midpoint), nums3[math.floor(midpoint)], nums3[math.ceil(midpoint)])
    median = (nums3[midpoint] + nums3[midpoint - 1]) / 2.0 if len(nums3) % 2 == 0 else nums3[int(midpoint)]

    return median


# print(median_of_two_sorted_arrays_4([1,3], [2]))

def roman_to_integer_13(s: str) -> int:
    roman_vals: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, "C": 100, 'D': 500, 'M': 1000}
    value = 0
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            value += roman_vals[s[i]]
            i += 1
        elif roman_vals[s[i]] < roman_vals[s[i + 1]]:
            value += roman_vals[s[i + 1]] - roman_vals[s[i]]
            i += 2
        else:
            value += roman_vals[s[i]]
            i += 1
    return value

    # for i in range(len(s)):
        # if i == 0:
        #     continue
        # if i > 0 and roman_vals[s[i - 1]] < roman_vals[s[i]]:
        #     value += roman_vals[s[i]] - roman_vals[s[i - 1]]
        # elif i == len(s) - 1:
        #     value += roman_vals[s[i - 1]] + roman_vals[s[i]]
        # else:
        #     value += roman_vals[s[i - 1]]
    # return value


print(roman_to_integer_13("MCMXCIV"))

