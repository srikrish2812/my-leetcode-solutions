class Solution:
    def sum_dig(self, n):
        s = 0
        while n!=0:
            s+=n%10
            n=n//10
        return s
    
    def sum_pairs(self, l):
        l.sort()
        return l[-1]+ l[-2]


    def maximumSum(self, nums: List[int]) -> int:
        pair_sum = defaultdict(list)
        max_sum=-1
        l = len(nums)
        for i in range(l):
            s_i = self.sum_dig(nums[i])
            pair_sum[s_i].append(nums[i])
        print(pair_sum)
        for l in pair_sum.values():
            if len(l)>=2:
                print(sum(l))
                max_sum = max(max_sum, self.sum_pairs(l))
        return max_sum
            
