def palindrum(string, stop):
    start = 0
    stop = stop -1 
    while(start <= stop):
        if(string[start] != string[stop]):
            return False
        start += 1
        stop -= 1
    return True


palindrum_store = {}
s = "bbbb"
string_len_1 = len(s)

pali_len = 1
pali = s[0]
stop = False
for index in range(string_len_1):
    sub_str_start = 1
    string_len = string_len_1 - index
    print(f"CURENT start index is {index}, with start string of {s[index]}")
    print(f"CURENT tring_len is {string_len}")
    while(sub_str_start <= string_len):
        sub_str = s[index: (index + sub_str_start)]
        print(f"Testing substring: {sub_str}")
        print(f"with stop at: {sub_str_start}")
        is_palindrum = palindrum(sub_str, (sub_str_start))
        print(f"is palindrum test is: {is_palindrum}")
        if(is_palindrum and (sub_str_start > pali_len)):
            pali = sub_str
            pali_len = sub_str_start
            if(pali_len >= (string_len_1 - index)):
                stop = True
                print("Checking condition to stop")
                break
        sub_str_start += 1
    if(stop):
        break
    # sub_str_start = 1
print(pali)
