def power(base,exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base,exp-1)

res = power(2,4)
print(res)