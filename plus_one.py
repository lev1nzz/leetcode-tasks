from typing import List


class Solution:
    def plusOne(self, digits: List[int]):
        num = int(''.join(map(str, digits))) + 1
        digits_list = [int(d) for d in str(num)]
        return digits_list    
        
            

solution = Solution()
print(solution.plusOne(digits=[4,3,2,1]))