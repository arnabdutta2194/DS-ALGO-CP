def merge(intervals):
    if intervals == []:
        return []
    # intervals = sorted(intervals, key= lambda x:x[0])
    print(intervals)
    resultList = []
    for interval in intervals:
        if resultList == [] or resultList[-1][1] < interval[0]:
            resultList.append(interval)
        else:
            resultList[-1][1] = max(resultList[-1][1],interval[1])
    print(resultList)


merge([[1,3],[2,6],[8,12],[10,15]])