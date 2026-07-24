class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        ans = [0] * (2 * n)

        for i in range(len(ans)):
            ans[i] = nums[i % n]

        return ans