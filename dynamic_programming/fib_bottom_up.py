def fib(n):
    store = {}
    for k in range(n+1):
        fib_result = None
        if k <= 2:
            fib_result = 1
        else:
            first = k - 1
            second = k - 2
            fib_result = store[str(first)] + store[str(second)]
        store[str(k)] = fib_result
        
    return store[str(n)]

print("fibonacci result for 8: ", fib(8))