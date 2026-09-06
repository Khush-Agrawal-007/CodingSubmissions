class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] represents the number of ways to form the prefix t[:j]
        dp = [0] * (n + 1)
        
        # Base case: 1 way to form an empty string t (by deleting all characters)
        dp[0] = 1
        
        for i in range(1, m + 1):
            # Iterate backwards through t to avoid using values updated in the current outer loop
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    # We add the ways to form t[:j-1] (using the current character) 
                    # to the existing ways to form t[:j] (skipping the current character)
                    dp[j] += dp[j-1]
                    
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna