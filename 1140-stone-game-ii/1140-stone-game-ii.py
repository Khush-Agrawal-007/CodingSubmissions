class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums to quickly find the total remaining stones
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i, m):
            # Base case: no stones left
            if i >= n:
                return 0
                
            # Base case: player can take all remaining stones
            if i + 2 * m >= n:
                return suffix_sum[i]
                
            if (i, m) in memo:
                return memo[(i, m)]
                
            max_stones = 0
            
            # Try taking X piles, where 1 <= X <= 2*M
            for x in range(1, 2 * m + 1):
                # We want to maximize: (Total stones left) - (What the opponent gets)
                current_stones = suffix_sum[i] - dp(i + x, max(m, x))
                max_stones = max(max_stones, current_stones)
                
            memo[(i, m)] = max_stones
            return max_stones
            
        return dp(0, 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna