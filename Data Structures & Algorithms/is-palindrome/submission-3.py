class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        text = ''.join(char.lower() for char in s if char.isalnum())


        if not text:
            return True
            
        for i in range(len(text)//2 + 1):
            if text[i] != text[-i-1]:
                return False

        return True 

