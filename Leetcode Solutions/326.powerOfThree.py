def isPowerOfThree(n):
    if n == 1: return True
    elif n == 0: return False
    elif n%3 != 0: return False
    else:
        return isPowerOfThree(int(n/3))
    