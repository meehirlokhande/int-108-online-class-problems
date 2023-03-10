class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s=set()
        i=0
        j=len(nums)-1
        
        while i < j:
            mine = nums[i]
            maxe = nums[j]
            avg = (maxe+mine)/2
            s.add(avg)
            i += 1
            j -= 1
            
        return len(s)
