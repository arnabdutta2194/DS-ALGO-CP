def isPalindrome(strng):
    print(strng)
    if len(strng) == 0:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])
res = isPalindrome("tacocat")
print(res)