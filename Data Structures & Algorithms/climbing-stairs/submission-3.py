class Solution:
    def climbStairs(self, n: int) -> int:

        one, two = 1,1

        # idx (two)  (one)
        # 0    1      1     -> skip
        # 1    1      2     -> start
        # 2    2      3
        # 3    3      5
        # 4    5      8
        
        # skip first thats why n-1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one