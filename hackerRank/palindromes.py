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
print(palindrom(str.lower(string)))
