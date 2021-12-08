def fibonacci(n,d):
    if n in d:
        return d[n]
    elif n in [0,1]:
        ans = n
    else:
        ans = fibonacci(n-1,d) + fibonacci(n-2,d)
    d[n] = ans
    return ans
res = fibonacci(11,{})
print(res)