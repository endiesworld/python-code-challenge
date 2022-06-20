"""
    Let's use decorators to build a name directory! You are given some information about  people. 
    Each person has a first name, last name, age and sex. Print their names in a specific format 
    sorted by their age in ascending order i.e. the youngest person's name should be printed first. 
    For two people of the same age, print them in the order of their input.

    Input Format
        The first line contains the integer N, the number of people.
        N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

    Sample Input

        3
        Mike Thomson 20 M
        Robert Bustle 32 M
        Andria Bustle 30 F
        Sample Output

        Mr. Mike Thomson
        Ms. Andria Bustle
        Mr. Robert Bustle
"""
import operator

text_case = [['Mike', 'Thomson', '20', 'M'], [
    'Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]


def person_lister():
    def inner(people):
        # complete the function
        def operation(x):
            if x[-1] == 'M':
                x.insert(0, 'Mr.')
            else:
                x.insert(0, 'Ms.')
            return x[:3]

        def formater(x):
            x[-2] = int(x[-2])
            return x
        people = list(map(formater, people))
        getcount = operator.itemgetter(2)
        people = sorted(people, key=getcount)
        people = list(map(operation, people))
        ans = [' '.join(data) for data in people]
        return ans
    return inner


example = person_lister()
print(example(text_case))
