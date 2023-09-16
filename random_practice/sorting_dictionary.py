my_list = list(range(-5, 6))
print(my_list)
custom_sorted = sorted(my_list, key=lambda arg : arg * arg) 
print(custom_sorted)