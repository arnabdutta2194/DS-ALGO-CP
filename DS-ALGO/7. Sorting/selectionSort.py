def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1,len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i] , customList[min_index] = customList[min_index], customList[i]
    return customList

cList = [5,9,3,1,2,8,4,7,6]
print(selectionSort(cList))

#-- Time Complexity - O(n^2)
#-- Space Complexity - O(1)