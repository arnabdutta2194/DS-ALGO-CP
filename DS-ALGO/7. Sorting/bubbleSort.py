def bubbleSort(customList):
    for i in range(len(customList)-1):  #----> O(n)
        for j in range(len(customList)-i-1): #----> O(n)
            if customList[j] > customList[j+1]:
                customList[j] , customList[j+1] = customList[j+1], customList[j]
    return customList

cList = [5,9,3,1,2,8,4,7,6]
print(bubbleSort(cList))

#-- Time Complexity - O(n^2)
#-- Space Complexity - O(1)