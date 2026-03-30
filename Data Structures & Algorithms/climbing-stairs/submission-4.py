class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1,1

        # idx (two)  (one)
        # x    1      1     -> skip
        # 0    1      2     -> start
        # 1    2      3
        # 2    3      5
        # 3    5      8
        
        # skip first thats why n-1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one