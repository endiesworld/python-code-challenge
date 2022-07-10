n = [4, 5, 35, 46]


def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)


print(fib(n[3]))
