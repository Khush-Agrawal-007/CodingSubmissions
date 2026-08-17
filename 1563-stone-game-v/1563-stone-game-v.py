from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # Precompute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i: int, j: int) -> int:
            return prefix[j + 1] - prefix[i]

        # dp[i][j] = max score for subarray i to j
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] = max(dp[i][k] + sum(i..k)) for k in i..j
        max_l = [[0] * n for _ in range(n)]
        # max_r[i][j] = max(dp[k][j] + sum(k..j)) for k in i..j
        max_r = [[0] * n for _ in range(n)]

        # Base cases: length 1 subarrays
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        # Bottom-up DP: Process lengths from 2 to n
        for i in range(n - 1, -1, -1):
            m = i - 1  # m is our sliding split pointer
            
            for j in range(i + 1, n):
                # Slide m to the right as long as left_sum <= right_sum
                while m + 1 < j and get_sum(i, m + 1) * 2 <= get_sum(i, j):
                    m += 1
                
                ans = 0
                if m >= i:
                    # If there's an exact tie, Alice can pick the best from either the left or right halves
                    if get_sum(i, m) * 2 == get_sum(i, j):
                        ans = max(ans, max_l[i][m], max_r[m + 1][j])
                    else:
                        # Otherwise, left_sum < right_sum for k <= m
                        ans = max_l[i][m]
                        
                        # For k > m, left_sum > right_sum, so Bob forces the right half
                        if m + 1 < j:
                            ans = max(ans, max_r[m + 2][j])
                else:
                    # If m < i, left_sum > right_sum for ALL possible splits
                    ans = max_r[i + 1][j]
                
                dp[i][j] = ans
                
                # Update our max prefix arrays for future lookups
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + get_sum(i, j))
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + get_sum(i, j))

        return dp[0][n - 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna