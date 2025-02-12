class Solution:
    def sum_dig(self, n):
        s = 0
        while n!=0:
            s+=n%10
            n=n//10
        return s

    def maximumSum(self, nums: List[int]) -> int:
        pair_sum = defaultdict(list)
        max_sum=-1
        l = len(nums)
        for num in nums:
            s_i = self.sum_dig(num)
            pair_sum[s_i].append(num)

            # this way we only retain the maximum two numbers in a list
            if len(pair_sum[s_i])>2:
                pair_sum[s_i].remove(min(pair_sum[s_i]))
            
        print(pair_sum)
        for l in pair_sum.values():
            if len(l)>=2:
                max_sum = max(max_sum, sum(l))

        return max_sum
            
