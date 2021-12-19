def merge(customList, l , m , r ):
    #-- l : First Index
    #-- m : Mid Index
    #-- r : Last Index
    n1 = m - l + 1  #-- Number of Elements in First SubArray
    n2 = r - m  #-- Number of Elements in Second SubArray
    L = [0] * n1  #-- Temporary Array for First SubArray
    R = [0] * n2  #-- Temporary Array for First SubArray

    #-- Divide Custom List into Two Sub Arrays
    #-- Add Elements to First Sub Array
    for i in range(0,n1):
        L[i] = customList[l+i]

    #-- Add Elements to First Second Array
    for j in range(0,n2):
        R[j] = customList[m+1+j]
    
    i = 0 #-- Initial Index of First SubArray
    j = 0 #-- Initial Index of Second SubArray
    k = l #-- Initail Index of Merged SubArray

    #--- Merge Arrays
    while i<n1 and j<n2:
        if L[i] <= R[j]: #-- Before Merging we have to put them in sorted order
            customList[k] = L[i]
            i+=1
        else:
            customList[k] = R[j]
            j+=1
        k += 1
    
    #-- Copy Remaining elements of L and R
    while i<n1:
        customList[k] = L[i]
        i += 1
        k += 1
    
    while j<n1:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList,l,r):
    if l < r:
        m = (l+(r-1))//2  # ---- O(1)
        mergeSort(customList,l,m)  #-- Call for First SubArray # ---- T(n/2)
        mergeSort(customList,m+1,r) #-- Call for Second SubArray # --- T(n/2)
        merge(customList,l,m,r) # --- O(n)
    return customList


cList = [5,3,4,7,2,8,6,9,1]
print(mergeSort(cList,0,len(cList)-1))

#-- Time Complexity - O(nlogn)
#-- Space Complexity - O(n)