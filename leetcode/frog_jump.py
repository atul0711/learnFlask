from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        k = 1
        for i in range(1, len(stones)):
            print(stones[i] - stones[i-1], k)
            if stones[i] - stones[i-1] in [k, k-1, k+1]:
                k = stones[i] - stones[i-1]
            elif stones[i] - stones[i-1] > k+1:
                return False
            elif stones[i] - stones[i - 1] < k or stones[i] - stones[i - 1] < k - 1:
                pass
        return True

obj = Solution()
print(obj.canCross([0,1,2,3,4,8,9,11]))
print(obj.canCross([0,1,3,5,6,8,12,17]))

