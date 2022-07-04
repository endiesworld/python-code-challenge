a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def list_reverser(list):
    new_list = list[:]
    mid = len(list) // 2

    for index in range(mid):
        new_list[index], new_list[-index -
                                  1] = new_list[-index - 1], new_list[index]
    return new_list


print(list_reverser(a_list))
