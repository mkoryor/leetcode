9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.




import sys 

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        num = x
        mod = 0
        reverse = 0
        
        while x > 0:
            mod = x % 10
            x = x // 10
            reverse = (reverse * 10) + mod
        
        if (reverse == num):
            return True
        else:
            return False
 
 
 
#test_case: 121
#result: True

