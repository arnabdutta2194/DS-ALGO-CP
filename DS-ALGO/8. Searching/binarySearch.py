import math
def binarySearch(customArray,value):
    start = 0
    end = len(customArray) - 1
    mid = math.floor((start + end)/2)
    if customArray[mid] == value:
        return mid

    while not(customArray[mid] == value) and start <= end:
        if value < customArray[mid]:
            # binarySearch(customArray[start:mid-1],value)
            end = mid - 1
        else:
            # binarySearch(customArray[mid+1:end],value)
            start = mid + 1
        mid = math.floor((start+end)/2)
        print(start,mid,end)
        if customArray[mid] == value:
            return mid
        else:
            return -1

custArray = [8,9,12,15,17,18,22,28]
print(binarySearch(custArray,122))