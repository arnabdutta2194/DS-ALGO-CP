import math
from insertionSort import insertionSort
def bucketSort(cusomList):
    lenList = len(cusomList)
    noOfBuckets = round(math.sqrt(lenList))
    maxValue = max(cusomList)
    arr = []

    for i in range(noOfBuckets):  # ----> O(n)
        arr.append([])

    for i in range(lenList): # ----> O(n)
        appropriateBucket = math.ceil((cusomList[i]*noOfBuckets)/maxValue)
        arr[appropriateBucket-1].append(cusomList[i])

    for i in range(noOfBuckets): # ----> O(n^2)  --- For Best Case we habe to use Quick Sort(nlogn)
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(noOfBuckets): # ----> O(n)
        for j in range(len(arr[i])):
            cusomList[k] = arr[i][j]
            k+=1
    
    return cusomList

cList = [5,3,4,7,2,8,6,9,1]
print(bucketSort(cList))

#-- Time Complexity - O(n^2)(For Insertion Sort)
#-- Time Complexity - O(nlogn)(For Quick/Merge Sort)
#-- Space Complexity - O(n)