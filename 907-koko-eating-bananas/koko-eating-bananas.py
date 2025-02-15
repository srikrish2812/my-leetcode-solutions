class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low =1
        high = max(piles)
        ans = max(piles)
        while low<=high:
            mid = low + (high-low)//2
            total_time = 0
            for ban in piles:
                total_time+=ceil(ban/mid)
            if total_time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        