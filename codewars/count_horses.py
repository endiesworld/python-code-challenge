def count_horses(sound_str):
    store = []
    last_index = 0
    counter = 1
    for index, dat in enumerate(sound_str):
        data = int(dat)
        if data: # Check for value
            if ((not (counter in store)) and (not (counter + last_index) in store)) : # Check if this is the first value
                
                for i in range(data):
                    store.append(counter + last_index)
                    print("counter value added: ", counter)
                    print("counter value added: ", counter + last_index)
            
            last_index = counter
            counter = 1
        else:
            counter += 1
    return store

if __name__ == '__main__':
    print(count_horses('122213122213122'))
    #print(count_horses('0212030212'))