from typing import *

def appleAndCoupon(n: int, m : int, arr: List[int])-> int:
    # Write your code here.
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                temp = arr[j]
                arr[j]=arr[i]
                arr[i] = temp
    print(arr)
    arr = arr[0:m-1] + arr[m:]
    return sum(arr)




# print(appleAndCoupon(5,3,[5,2,4,1,3]))
print(appleAndCoupon(2,2,[3,2]))