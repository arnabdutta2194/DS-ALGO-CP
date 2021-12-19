def insertionSort(customList):
    for i in range(1,len(customList)): 
        key = customList[i]
        j = i-1 #Element Before Key  
        while j >=0 and key < customList[j]:  
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

cList = [5,3,4,7,2,8,6,9,1]
# print(insertionSort(cList))

#-- Time Complexity - O(n^2)
#-- Space Complexity - O(1)