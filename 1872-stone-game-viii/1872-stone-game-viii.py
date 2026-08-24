class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Step 1: Calculate prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i-1]
            
        # Step 2: Initialize DP with the base case (taking all stones)
        res = stones[-1]
        
        # Step 3: Iterate backwards from the second to last element down to index 1
        # Index 0 is excluded because players must take x > 1 stones.
        for i in range(n-2, 0, -1):
            res = max(res, stones[i] - res)
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna