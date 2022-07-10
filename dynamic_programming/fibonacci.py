def exponential(a, n):
    if n == 0:
        return 1
    return (a * exponential(a, n-1))


# print(exponential(2, 8))
n = [4, 5, 7, 35, 46]

#  Version I fibonacci solution


def fib(n):
    store = {
        1: 1,
        0: 0
    }
    if n in store.keys():
        return store[n]
    return fib(n-1) + fib(n-2)


print(fib(n[2]))
