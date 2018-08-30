Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Seen this question in a real interview before?  
Difficulty:Medium
Total Accepted:196.1K
Total Submissions:604.4K
Contributor:LeetCode
Subscribe to see which companies asked this question.

Related Topics 

Similar Questions 
3Sum3Sum Smaller
Python3	

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        count = 0
        left = nums[:4]
        right = nums[0:]
        middle = nums[:]
        
        for i in range(len(nums)):
            for j 
            
            



            
