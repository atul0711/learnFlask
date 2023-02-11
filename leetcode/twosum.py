from typing import List
#10/12
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = 0
        num_list=[]
        for i in range(len(nums)):
            if target < nums[i]:
                pass
            else:
                holder += nums[i]
                num_list.append(i)
            if len(num_list) > 2:
                del num_list[0]
            if holder == target:
                return num_list
            else:
                temp = holder
                temp -= nums[i]
                holder -= temp

# test Cases
obj = Solution()
print(True if obj.twoSum([2,7,11,15], 9) == [0,1] else False)
print(True if obj.twoSum([3,2,4], 6) == [1,2] else False)
print(True if obj.twoSum([3,2,3], 6) == [0,2] else False)
