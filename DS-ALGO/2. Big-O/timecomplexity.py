#--- Q1
def foo(arr):
    sum = 0   #----- O(1)
    product = 1 #----- O(1)
    for i in arr: #----- O(n)
        sum += i
    
    for i in arr: #----- O(n)
        product *= i

    print("Sum = "+str(sum)+", Product = "+str(product)) #----- O(1)

''' 
Total Time Complexity : O(1) + O(1) + O(n) + O(n) + O(1) = O(2n) = O(n)
'''

#--- Q2
def printPairs(arr):
    for i in arr:  #----- O(n)
        for j in arr:  #----- O(n)
            print(str(i) + "," + str(j)) #----- O(1)

''' 
Total Time Complexity : O(n) * O(n) = O(n^2)
'''

#--- Q3
def printUnorderedPairs(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            print(arr[i]+" ,"+arr[j])

# Outer Loop - n times
# 1st Iteration (Inner Loop) -- n-1
# 2st Iteration (Inner Loop) -- n-2
# ..... last iteration (Inner Loop) -- 1

# Therefore summing up : (n-1)+(n-2)+(n-3) + .... +2 + 1 = n(n-1)/2
# = n^2/2 + n
# After removing non-dominant terms -- O(n^2)

#--- Q4
def printUnorderedPairs(arrA,arrB):
    for i in range(len(arrA)):  #--- O(a)
        for j in range(len(arrB)): #--- O(b)
            for k in range(0,100000): #--- O(10000) -- O(1)
                print(str(arrA[i]) + "," + str(arrB[j]))

''' 
Total Time Complexity : O(a) * O(b) = O(ab)
'''

#--- Q5
def reverse(arr):
    for i in range(0,int(len(arr)/2)): #--- O(n/2)
        end = len(arr) - i - 1 #--- O(1)
        start = arr[i] #--- O(1)
        arr[i] = arr[end] #--- O(1)
        arr[end] = start #--- O(1)
    print(arr) #--- O(1)
 
''' 
Total Time Complexity : O(n/2) + O(1) + O(1) + O(1) + O(1) + O(1) = O(n)
'''

#--- Q6
def factorial(n):  
    if n < 0:   #---- O(1)
        return -1
    elif n==0:   #---- O(1)
        return 1
    else:
        return n * factorial(n-1) #O(n)
''' 
Total Time Complexity : O(1) + O(1) + O(n) = O(n)
''' 

#--- Q7
def powersofTwo(n):
    if n<1: return 0  #---- O(1)
    elif n == 1: return 1  #---- O(1)
    else:
        prev = powersofTwo(int(n/2))   #---- O(log(n))
        curr = prev *2 #---- O(1)
        return curr #---- O(1)


''' 
Total Time Complexity : O(1) + O(1) + O(1) + O(1) + O(log(n)) = O(log(n))
'''