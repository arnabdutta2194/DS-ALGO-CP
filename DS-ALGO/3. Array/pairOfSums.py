def pairOfSums(list,target):
     for i in range(len(list)):
         for j in range(i+1,len(list)):
            if list[i] == list[j]:
                 continue
            elif list[i] + list[j] == target:
                return [i,j]
myList = [2,6,4,9,11]
target = 15
print(pairOfSums(myList,target))

# class Solution(object):
#     def twoSum(self, nums, target):
#         var_dict = {}
#         for index_num1,var in enumerate(nums): 
#             k = target - var
#             try: 
#                 index_num2 = var_dict[k]
#             except BaseException: 
#                 var_dict[var] = index_num1
#             else: 
#                 return tuple(sorted([index_num1, index_num2]))