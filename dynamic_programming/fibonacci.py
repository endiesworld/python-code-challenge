def exponential(a, n):
    if n == 0:
        return 1
    return (a * exponential(a, n-1))


# print(exponential(2, 8))
n = [4, 5, 7, 35, 46]

#  Version I fibonacci solution


def fib(n):
    return _fib(n,  store={
        1: 1,
        0: 0
    })


def _fib(n, store):
    if n in store:
        return store[n]
    store[n] = _fib(n-1, store) + _fib(n-2, store)
    return store[n]


print(fib(n[4]))
