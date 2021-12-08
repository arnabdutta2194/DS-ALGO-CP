myList = [1,2,3,4,5,7,8,9,10]
noOfIntegers = 10

def findMissingInteger(list,n):
    sum1 = int((n*(n+1))/2) 
    sum2 = sum(list)
    missingNumber = sum1 - sum2
    return missingNumber

print(findMissingInteger(myList,noOfIntegers))