class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product= nums[i]*nums[j]
                product_cnt[product]+=1
        ans=0
        for val in product_cnt.values():
            ans+= 8*(val*(val-1)//2)
        return ans