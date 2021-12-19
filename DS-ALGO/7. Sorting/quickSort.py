def partition(customList,low,high):
    # -- low --> First Index
    # -- high --> Last Index
    i = low - 1
    pivot = customList[high] # -- RightMost Element
    for j in range(low,high): # ---- O(n)
        if customList[j] <= pivot:
            i+=1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i+1],customList[high] = customList[high],customList[i+1]
    return (i+1)

def quickSort(customList,low,high):
    if low<high:
        partitionIndex = partition(customList,low,high) # --- O(n)
        quickSort(customList,low,partitionIndex-1) # --- T(n/2)
        quickSort(customList,partitionIndex+1,high) # T(n/2)
    return customList

cList = [3,5,8,1,2,9,4,7,6]
print(quickSort(cList,0,len(cList)-1))

#-- Time Complexity - O(nlogn)
#-- Space Complexity - O(n)