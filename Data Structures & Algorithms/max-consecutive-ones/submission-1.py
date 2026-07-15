class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current = 0
        max_val = 0

        for num in nums:
            if num == 1:
                current += 1
                max_val = max(max_val, current)
            else:
                current = 0


        return max_val