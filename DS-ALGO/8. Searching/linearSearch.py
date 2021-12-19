def linearSearch(customList,value):
    for _val in range(len(customList)):
        if customList[_val] == value:
            return _val
    return -1

customList = [5,9,3,1,2,8,4,7,6]
print(linearSearch(customList,2))
print(linearSearch(customList,22))