from typing import List

def singleNumber(nums: List[int]):
    new_list = []
    
    for i in nums:
        if i in new_list:
            new_list.remove(i)
        else:
            new_list.append(i)
    return new_list[0]
        
            
print(singleNumber(nums=[2,2,1]))