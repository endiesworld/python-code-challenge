# Use a generator function to read files in chunks
import os

# Get the current directory where the script is located
current_directory = os.path.dirname(__file__)

# Specify the relative path to your file
filename = 'test_file_read.txt'  # Change to your database file name

# Combine the current directory and the relative path to create the full path
complete_file_path = os.path.join(current_directory, filename)

def read_n(filename, chunk_size):

    try:
        f = open(filename)
        while True:
            each_chunk = ''.join(f.readline() for i in range(chunk_size))
            if each_chunk:
                yield each_chunk
            else:
                break
    except FileNotFoundError as e:
        print(f"No such file {filename}")
    except IsADirectoryError as e:
        print(f"No such directory {filename}")
    except UnicodeDecodeError as e:
        print(f"Could not decode {filename}")
        
    finally:
        f.close()
    


def read_n_2(filename, chunk_size):

    try:
        f = open(filename)
        while True:
            each_chunk = f.read(chunk_size)
            if each_chunk:
                yield each_chunk
            else:
                break
    except FileNotFoundError as e:
        print(f"No such file {filename}")
    except IsADirectoryError as e:
        print(f"No such directory {filename}")
    except UnicodeDecodeError as e:
        print(f"Could not decode {filename}")
        
# Read characters in chunk
for chunk in read_n_2(complete_file_path, 3):
    print(chunk)
    
# Read lines in chunks
for chunk in read_n(complete_file_path, 3):
    print(chunk)