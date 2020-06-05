# 198. House Robber
# Time Complexity : O(n) 
# Space Complexity : O(n) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# 
# Here In this problem, I have created a new array to store the intermediate results
# fisrtly i add nums[o] directly to my results array. Then compare the next element in nums with prev and add max value to result array
#will iterate through the array from 2nd index and check if max value between prev value in  result to that of current nums value + value 2 index away in the result array. dd the max #value to the results and return the last element in result.

class Solution:
    def rob(self, nums: List[int]) -> int:
        count = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        count.append(nums[0])
        count.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            count.append(max (count[i-1],count[i-2] + nums[i]))
            
        return count[-1]