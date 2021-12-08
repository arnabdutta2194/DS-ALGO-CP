def compression(chars):
    count = 1
    resultList = []
    for i,data in enumerate(chars):
        if (i+1)< len(chars) and chars[i+1] == data:
            count += 1
        else:
            if count == 1: resultList.append(chars[i])
            else : resultList.extend([chars[i-1],count])
            count = 1
    return resultList

resultList = compression(["a"])
print(resultList)


# def compression(chars):
#     count = 1
#     j = 0
#     for i in range(1,len(chars)+1):
#         if i < len(chars) and chars[i] == chars[i-1]:
#             count += 1
#         else:
#             chars[j] = chars[i-1]
#             j += 1
#             if count > 1:
#                 for k in str(count):
#                     chars[j] = k
#                     j+=1
#             count = 1
#     return j

resultList = compression(["a","a","b","a","a"])
print(resultList)