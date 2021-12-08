def checkPermutation(myList1,myList2):
    if len(myList1) != len(myList2):
        return False
    elif sorted(myList1) == sorted(myList2):
        return True
    else:
        return False
print(checkPermutation([2,1,3],[2,1,3]))