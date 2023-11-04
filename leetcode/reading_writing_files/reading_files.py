import os

# Get the current directory where the script is located
current_directory = os.path.dirname(__file__)

# Specify the relative path to your file
filename = 'test_file_read.txt'  # Change to your database file name

# Combine the current directory and the relative path to create the full path
complete_file_path = os.path.join(current_directory, filename)

def numbers_of_vowels(filename):
    count = 0
    try:
        # loping over the file object. But this is bad because I can't close the file
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

# with open('test_write_file.txt', 'w') as f:
#     f.write('My name is Emmanuel Okoro\n')
#     f.write('I am a full-stack dev from Nigeria')


def numbers_of_vowels_2(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            for char in line:
                if char in 'aeiouAEIOU':
                    count += 1
    return count

# print(numbers_of_vowels("test_write_file.txt"))
# print(numbers_of_vowels(complete_file_path))

print(numbers_of_vowels_2(complete_file_path))