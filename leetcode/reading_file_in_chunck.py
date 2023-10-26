# Use a generator function to read files in chunks

def read_n(filename, chunk_size):
    f = open(filename)
    
    while True:
        each_chunk = ''.join(f.readline() for i in range(chunk_size))
        if each_chunk:
            yield each_chunk
        else:
            break
        

for chunk in read_n("test_file.txt", 3):
    print(chunk)