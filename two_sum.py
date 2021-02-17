class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # maintain a mapping like (key: value) - (number: index)
        # check if (target - num) has already been found
        
        num_index = {}
        
        for i, num in enumerate(nums):
            
            if target-num in num_index:
                return [num_index[target-num], i]
            num_index[num] = i
            
        return []
