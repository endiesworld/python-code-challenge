def numberOfWeakCharacters(properties):
    prop_len = len(properties)
    index = 0
    result = 0
    while index+1 < prop_len:
        if ((properties[index][0] <= properties[index + 1][0]) and (properties[index][1] < properties[index + 1][1])) or ((properties[index][0] > properties[index + 1][0]) and (properties[index][1] > properties[index + 1][1])):
            result += 1
            print('First condition met')
        elif ((properties[index][0] < properties[index + 1][0]) and (properties[index][1] < properties[index + 1][1])) or ((properties[index][0] > properties[index + 1][0]) and (properties[index][1] > properties[index + 1][1])):
            result += 1
            print('second condition met')

        index += 1
    return result


properties = [[2, 2], [3, 3]]
properties = [[1, 5], [10, 4], [4, 3]]
properties = [[5, 5], [6, 3], [3, 6]]
properties = [[1, 1], [2, 1], [2, 2], [1, 2]]
properties = [[7, 7], [1, 2], [9, 7], [7, 3], [
    3, 10], [9, 8], [8, 10], [4, 3], [1, 5], [1, 5]]
print(numberOfWeakCharacters(properties))
