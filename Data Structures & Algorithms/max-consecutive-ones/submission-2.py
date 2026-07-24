class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        final = 0


        for i in range(len(nums)):
            if nums[i] == 1:
                currentMax += 1
            else:
                final = max(final, currentMax)
                currentMax = 0
            final = max(final, currentMax)
        
        
        return final

     