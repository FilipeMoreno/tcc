class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the integer to a string
        str_x = str(x)
        
        # Check if the string is the same when read backward
        return str_x == str_x[::-1]
