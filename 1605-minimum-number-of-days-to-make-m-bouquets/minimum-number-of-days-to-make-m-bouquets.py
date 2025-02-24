class Solution:
    def num_bouquets(self, arr,k,d):
        count=0
        bouquets=0
        for i in range(len(arr)):
            if arr[i]<=d:
                count+=1
                if count==k:
                    bouquets+=1
                    count=0
            else:
                count=0
        return bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay)
        ans = max(bloomDay)
        n = len(bloomDay)
        if n<m*k: return -1
        while low<=high:
            mid = low + (high-low)//2
            if self.num_bouquets(bloomDay,k,mid)>=m:
                ans=mid
                high=mid-1 # ensures we are moving towards the minimum value of days to make it happen
            else:
                low=mid+1
        return ans