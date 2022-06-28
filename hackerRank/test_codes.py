def binary_search(elements, string_val):

    if len(elements) == 1:
        return 0 if elements[0] == string_val else None

    mid = len(elements) // 2
    if string_val == elements[mid]:
        return mid

    if string_val < elements[mid]:
        return binary_search(elements[:mid], string_val)
    else:
        try:
            return mid + binary_search(elements[mid:], string_val)
        except TypeError as e:
            return 'Value not found'


print(binary_search([1, 2, 3, 4, 4, 6, 7, 8, 9, 10], 5))
