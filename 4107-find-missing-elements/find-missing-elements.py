class Solution:
    def findMissingElements(self, nums):
        start=min(nums)
        end=max(nums)
        s=set(nums)
        ans=[]
        for i in range(start,end+1):
            if i not in s:
                ans.append(i)
        return ans