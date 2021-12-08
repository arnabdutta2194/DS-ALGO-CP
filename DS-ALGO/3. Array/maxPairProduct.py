def maxProductPair(myList):
    maxProd = 0
    if len(myList) == 0: return 0
    for _i in range(len(myList)):
        for _j in range(_i+1,len(myList)):
            if myList[_i] * myList[_j] > maxProd:
                maxProd = myList[_i] * myList[_j]
    return maxProd

print(maxProductPair([4,3,2,5]))
