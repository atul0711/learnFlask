class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        if n <= 1 or n >= 45:
            return 0
        else:
            two_steps = n//2
            remain = n%2
            if  two_steps != 0:
                ways += 1
            if remain != 0:
                ways += 1
        print(ways)

obj = Solution()
obj.climbStairs(3)