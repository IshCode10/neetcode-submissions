class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current_value = 0
        max_value = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                current_value += 1
            else:
                max_value = max(max_value, current_value)
                current_value = 0
        max_value = max(max_value, current_value)

        return max_value
