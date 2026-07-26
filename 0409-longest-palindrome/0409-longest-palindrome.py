class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired = set()
        length = 0
        
        for char in s:
            if char in unpaired:
                length += 2
                unpaired.remove(char)
            else:
                unpaired.add(char)
                
        # If any single characters remain, we can put one in the center
        if unpaired:
            length += 1
            
        return length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna