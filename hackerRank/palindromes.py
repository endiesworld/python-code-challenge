from itertools import count
from unittest import result


def palindrom(string):
    first_index = 0
    second_index = len(string) - 1
    return _palindrom(string, first_index, second_index)


def _palindrom(string, first_index, second_index):
    if first_index > second_index:
        return True

    first_str = string[first_index]
    second_str = string[second_index]
    first_index = first_index + 1
    second_index = second_index - 1
    result = _palindrom(string, first_index, second_index)
    if result:
        return first_str == second_str

    return False


string = 'noeaon'
string = 'level'
# print(palindrom(str.lower(string)))


def longestPalindrome(s: str) -> str:
    pal_length = 0
    pal = ''
    str_len = len(s)
    main_count = 0
    memory = []
    while main_count < str_len:
        base_str = s[main_count:]
        if pal_length < (str_len - main_count):
            sub_count = 0
            balance_len = str_len - main_count
            while sub_count < balance_len:
                sub_str = ''
                if sub_count == 0:
                    sub_str = base_str
                else:
                    sub_str = base_str[:-sub_count]
                passed_len = str_len - main_count - sub_count
                result = small_palindrom(sub_str, passed_len)
                if result:
                    print('pal test passed')
                    new_length = len(sub_str)
                    if new_length > pal_length:
                        pal_length = new_length
                        pal = sub_str
                    break
                sub_count += 1
            main_count += 1
        else:
            break

    return pal


def small_palindrom(s, str_len):
    is_pal = True
    count = 0
    while count < str_len:
        if s[count] != s[-1 - count]:
            is_pal = False
            break
        count += 1
    return is_pal


# string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(longestPalindrome(string))
# print(string[:-0])
# print(string[:-1])
# print(string[:-2])

# print(small_palindrom(string))
