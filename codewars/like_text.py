def likes(names):
    # your code here
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return '{} like this'.format(names[0])
    if len(names) == 2:
        return '{} and {} like this'.format(names[0],names[1])
    if len(names) == 3:
        return '{}, {} and {} like this'.format(names[0],names[1],names[2])
    else:
        others = str(len(names) - 2)
        return '{}, {} and {} others like this'.format(names[0],names[1], others)
    

def likes(names):

    message_store = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
   
    return message_store[min(4, length)].format(*names, others = length - 2)


def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

    
if __name__ == '__main__':
    print(likes([]))
    print(likes(['Peter']))
    print(likes(['Jacob', 'Alex']))
    print(likes(['Max', 'John', 'Mark']))
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))