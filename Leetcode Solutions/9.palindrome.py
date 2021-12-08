import re
def isPalindrome(inputStr):
    # newStr = re.sub('^[A-Za-z0-9]+','',inputStr)
    newStr = re.sub(r'\W+','',inputStr)
    newStr = newStr.replace(" ","").lower()
    print(newStr)
    

    if newStr == newStr[::-1]:
        return "Yes, its Palindrome"
    else:
        return "No, its not a Palindrome"


returnVal = isPalindrome("Mr. Owl ate my metal worm")
print(returnVal)


### --- Leetcode Problem Solution --- ###
class Solution:
    def isPalindrome(self, x: int) -> bool:
        data = str(x)
        if len(data) < 0 : return False
        if data == data[::-1]: return True
        else: return False