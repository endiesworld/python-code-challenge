def duplicate_count(text):

    if not text:
        return 0
    counter = 0
    store = {}
    text = text.lower()
    for data in text:
        store[data] = store.get(data, 0) + 1
    for key, value in store.items():
        if value > 1:
            counter += 1
    return counter

if __name__ == '__main__':
    print(duplicate_count("") == 0)
    print(duplicate_count("abcde") == 0)
    print(duplicate_count("abcdeaa")== 1)
    print(duplicate_count("abcdeaB") == 2)
    print(duplicate_count("Indivisibilities") == 2)