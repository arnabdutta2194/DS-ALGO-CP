def isPowerOfFour(n):
    if n == 1: return True
    elif n == 0: return False
    elif n%4 != 0: return False
    else:
        return isPowerOfFour(int(n/4))
    