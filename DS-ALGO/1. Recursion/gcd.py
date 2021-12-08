def gcdeuclid(a,b):
    if b == 0:
        return a
    else:
        return gcdeuclid(b,a%b)

res = gcdeuclid(48,18)
print(res)