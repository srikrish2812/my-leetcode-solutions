class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        ans = cur_sum
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            ans = max(ans, cur_sum)
        return ans

        