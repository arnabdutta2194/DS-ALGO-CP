def isPalindrome(strng):
    print(strng)
    # Base case: if the string is empty or has one character
    if len(strng) == 0:
        return True
    
    # Check first and last characters
    if strng[0] != strng[-1]:
        return False
    
    # Recursive case: check the substring without the first and last characters
    return isPalindrome(strng[1:-1])

res = isPalindrome("tacocat")
print(res)