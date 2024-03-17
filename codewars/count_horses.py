"""
DESCRIPTION:
A group of horses just ran past Farmer Thomas, and he would like to figure out how many horses were there. However, Farmer Thomas has a bad eye sight, and cannot really see the horses that are now distant. He did remember the sound of their galloping though, and he wants your help in figuring out how many horses (and the length of their legs) were in that group.

Each horse will make a thumping noise every step as its hooves hit the ground. Farmer Thomas has recorded the sound as strings like this (the following record is 15 seconds long):
000100010001000
"""

    
def count_horses(sound_str):
    store = []
    for index, dat in enumerate(sound_str):
        data = int(dat)
        if data: # Check for value
            horses = data
            for data_stored in store:
                if (index + 1)% data_stored == 0: # Check if horse has been counted previously
                    horses -= 1 # Remove previously counted horse from existing list
                if horses == 0:
                    break
            for i in range(horses): # Check if ther are still uncounted horse
                store.append(index+1)
    return store
                    
                    

if __name__ == '__main__':
    # print(count_horses('122213122213122'))
    print(count_horses('0212030212'))
    print(count_horses('0111020111'))
    print(count_horses('0001000100010001000100'))
    