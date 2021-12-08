def dectobin(n):
    if n == 0:
        return 0
    return n%2 + 10 * dectobin(int(n/2))

res = dectobin(10)
print(res)