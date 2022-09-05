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
    for index, char in enumerate(s):
        base_str = s[index:]
        if pal_length < len(base_str):
            for sub_index, sub_char in enumerate(base_str):
                sub_str = ''
                if sub_index == 0:
                    sub_str = base_str
                else:
                    sub_str = base_str[:-sub_index]
                result = palindrom(sub_str)
                if result:
                    new_length = len(sub_str)
                    if new_length > pal_length:
                        pal_length = new_length
                        pal = sub_str
                    break
        else:
            break

    return pal


string = "cbbd"
print(longestPalindrome(string))
# print(string[:-0])
# print(string[:-1])
# print(string[:-2])
