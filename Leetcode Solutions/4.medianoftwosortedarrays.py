import math
def findMedian(nums1,nums2):
    mergedArray = sorted(nums1 + nums2)
    N = len(mergedArray)
    if N%2 == 0:
        return (mergedArray[int(math.floor((N-1)//2))] + mergedArray[int((N)//2)])/2
    else:
        return mergedArray[(N-1)//2]
            

data = findMedian([1,2],[3,4])
print(data)