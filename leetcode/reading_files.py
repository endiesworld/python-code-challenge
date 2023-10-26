def numbers_of_vowels(filename):
    count = 0
    try:
        for each_line in open(filename, 'r', encoding='UTF-8'):
            for each_char in each_line:
                if each_char in 'aeiouAEIOU':
                    count += 1
    except FileNotFoundError as e:
        print(f"No such file {filename}")
    except IsADirectoryError as e:
        print(f"No such directory {filename}")
    except UnicodeDecodeError as e:
        print(f"Could not decode {filename}")
        
    return count

with open('test_write_file.txt', 'w') as f:
    f.write('My name is Emmanuel Okoro\n')
    f.write('I am a full-stack dev from Nigeria')


print(numbers_of_vowels("test_write_file.txt"))
print(numbers_of_vowels("test_file.txt"))
