
def isPowerOfTwo(self, n: int) -> bool:
    if n == 1: return True
    elif n == 0: return False
    elif n%2 != 0: return False
    else:
        return isPowerOfTwo(int(n/2))

s = ['a','b','c']
print(s[-1:])