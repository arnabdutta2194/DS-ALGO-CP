# def flattenArray(arr):
#     resultArr = []
#     for val in arr:
#         if type(val) is list:
#             resultArr.extend(flattenArray(val))
#         else:
#             resultArr.append(val)
#     return resultArr

# res = flattenArray([1, [2, [3, 4], [[5]]]])
# print(res)

def flattenArray(nestedList):
    if not(bool(nestedList)):
        return nestedList
    if isinstance(nestedList[0],list):
        return flattenArray(*nestedList[:1]) + flattenArray(nestedList[1:])
    return nestedList[:1] + flattenArray(nestedList[1:])

res = flattenArray([1, [2, [3, 4], [[5]]]])
print(res)