7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:

Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
      
        
        reverse = 0
        num = x
        
        if(x < 0):
            x = -x
            
        while x > 0:
            remain = x % 10 # use modulo to make the remainder an exact integer
            reverse = (reverse * 10) + remain
            x = x // 10  #floor the num to be an exact integer
            
        if num < 0:
            reverse = -reverse
        if reverse > 2147483647 or reverse < -2147483647:
            return 0
        return reverse
        
        
#test_case: 222
#result: 222
        
        

