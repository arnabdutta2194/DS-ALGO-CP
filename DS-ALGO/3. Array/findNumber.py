from typing import no_type_check


def binarySearch(myList,num,l,r):
    
    if r >= 1:  
        mid = l + (r-1)//2
        if myList[mid] == num:
            return mid
        elif myList[mid] > num:
            return binarySearch(myList,num,l,mid-1)
        else:
            return binarySearch(myList,num,mid+1,r)
    else:
        return "Not Found"

myList = [12,4,56,76,102,122,290]
num = 102
l = 0
r = len(myList)-1

print(binarySearch(myList,num,l,r))


