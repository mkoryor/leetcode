


14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        

        if strs == []: 
            return ''
        
        
       
        
        first = min(strs)
        second = max(strs)
        
        for index, letter in enumerate(first): # gives string there indexes for example in "first" (0, f), (1, i).....exc
            if letter != second[index]:  # check if letter is equal to max(wordletter)
                return first[0:index] 
                
        return first 
        
        
        
#test_case: ["flower", "flow", "flight"]       
#output: "fl"


