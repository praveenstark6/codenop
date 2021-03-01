class Solution:
    def fib(self, n: int) -> int:
        # 0 1 1 2 3 5 8 13....
        
        i = 0
        j = 1
        for _ in range(n):
            i, j = j, i+j
        return i
