class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
        
solution = Solution()
print(solution.addDigits(num=38))  