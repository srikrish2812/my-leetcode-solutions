class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs=defaultdict(int)
        n = len(nums)
        for num in nums:
            pairs[num]+=1
        total=0
        for count in pairs.values():
            total+=count*(count-1)/2
        return int(total)
        
