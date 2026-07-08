class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        MOD = 10**9 + 7
        
        # Precompute powers of 10 modulo 10^9 + 7
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        sumD = [0] * (n + 1)
        cntN0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        # Build the prefix arrays
        for i, char in enumerate(s):
            d = int(char)
            sumD[i + 1] = sumD[i] + d
            cntN0[i + 1] = cntN0[i] + (1 if d > 0 else 0)
            
            if d > 0:
                p[i + 1] = (p[i] * 10 + d) % MOD
            else:
                p[i + 1] = p[i]
                
        ans = []
        for l, r in queries:
            sd = sumD[r + 1] - sumD[l]
            n0 = cntN0[r + 1] - cntN0[l]
            
            # Calculate x and ensure it is positive
            x = (p[r + 1] - p[l] * pow10[n0]) % MOD
            if x < 0:
                x += MOD
                
            res = (x * sd) % MOD
            ans.append(res)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna