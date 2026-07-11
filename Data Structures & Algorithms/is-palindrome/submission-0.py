class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        text = ''.join(char.lower() for char in s if char.isalnum())
        reverseText = text[::-1]

        return True if text == reverseText else False

