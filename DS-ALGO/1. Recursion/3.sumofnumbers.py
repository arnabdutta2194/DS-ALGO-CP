def sumOfNumbers(n):
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfNumbers(int(n/10))

res = sumOfNumbers(15511)
print(res)