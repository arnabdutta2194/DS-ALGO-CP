def uniqueElements(myList):
    uniqList = []
    for _var in myList:
        if _var not in uniqList:
            uniqList.append(_var)
        else:
            return "Not Unique"
    return "Unique"

print(uniqueElements([2,99,99,12,3,11,223]))