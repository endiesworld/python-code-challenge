"""
Be Concise IV - Index of an element in an array
Task
Provided is a function Kata which accepts two parameters in the following order: array, element and returns the index of the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the strict character count requirements of the Kata. (no more than 161) You may assume that all array elements are unique.

"""
array1 = [2,3,5,7,11]
array = [True, 'Hello World', False, 'Lorem Ipsum', 6, 'pi']

def find(a, e):
    return a.index(e) if e in a else "Not found"

if __name__ == "__main__":
    assert(find(array, 5), 2)
    assert(find(array, 11), 4)
    assert(find(array, 3), 1)
    assert(find(array, 2), 0)
    assert(find(array, 7), 3)
    assert(find(array, 1), 'Not found')
    assert(find(array, 8), 'Not found')

        
    assert(find(array, 'Hello World'), 1)
    assert(find(array, 'lorem ipsum'), 'Not found')
    assert(find(array, 'Lorem Ipsum'), 3)
    assert(find(array, False), 2)
    assert(find(array, True), 0)
    assert(find(array, 'pi'), 5)
    assert(find(array, 3.14), 'Not found')
    assert(find(array, 6), 4)
    