class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        
        for i in range(n):
            ones_count = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones_count += 1
                
                # Once we hit exactly k ones, evaluate the substring
                if ones_count == k:
                    sub = s[i:j+1]
                    if not ans:
                        ans = sub
                    elif len(sub) < len(ans):
                        ans = sub
                    elif len(sub) == len(ans) and sub < ans:
                        ans = sub
                # No need to keep going if we've exceeded k ones
                elif ones_count > k:
                    break
                    
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna