def factorial(n):
    assert n >= 1 and int(n) == n , "n should be a positive integer"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

res = factorial(5)
print(res)