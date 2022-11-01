def lengthOfLongestSubstring(s):
    # str_len = len(s)
    # store = {}
    # length = 0
    # maximum = 0

    # for index, char in range(str_len):
    #     length = 1
    #     store[char] = char
    #     for char2 in s[index+1:]:
    #         if (char2 in store):
    #             store = {}
    #             break
    #         length += 1
    #         store[char2] = char2

    #     maximum = max( maximum ,length)
    #     print('maximum lenght:', maximum)
    #     if maximum >= str_len - index:
    #         break

    # return maximum

    #     store = {}
    #     ref_index = 0
    #     pointer = 0
    #     maximum = 0

    #     for index, char in enumerate(s):
    #         if (char not in store):
    #             store[char] = index
    #             pointer = index
    #         else:
    #             print('**********************************')
    #             print('store: ', store)
    #             print('ref_index: ', ref_index)
    #             print('pointer: ', pointer)
    #             print('maximum: ', maximum)
    #             maximum = max(maximum, (pointer - ref_index))
    #             ref_index = store[char] + 1
    #             store[char] = index

    #     if(pointer == 0):
    #         return 0

    #     return max(maximum, ((pointer - ref_index)))
    pass

# print(lengthOfLongestSubstring("abcabcbb"))


# def FindIntersection(strArr):

#     # code goes here
#     store = []
#     myDict = {}
#     second = {}
#     for char in strArr[0].split(', '):
#         myDict[char] = char
#     for char in strArr[1].split(', '):
#         if ((char in myDict) and (char not in second)):
#             store.append(char)
#             second[char] = char
#     return store


# # keep this function call here
# print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))

# print("1, 3, 4, 7, 13".split(', '))

def MinWindowSubstring(strArr):

    # code goes here
    store = {}
    index_ref = [strArr[0]]
    ref_store = {}
    last_index = -1
    new_string = ''
    empty = True
    start = 0
    stop = 0
    for char in strArr[1]:
        ref_store[char] = char
    ref_store_1 = ref_store

    for index, char in enumerate(strArr[0]):
        if(index - 1 >= 0):
            if (char in ref_store_1):
                index_ref.append(char)

    for index in index_ref:
        new_string += strArr[0][index]

    return new_string


# keep this function call here
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
