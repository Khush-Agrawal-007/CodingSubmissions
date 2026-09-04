class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if not nums:
            return -1
            
        # Precompute the minimum values from the right (suffix minimums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
            
        prefix_max = float('-inf')
        
        # Traverse from the left, tracking the running maximum
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            
            # Check the stability condition
            if prefix_max - suffix_min[i] <= k:
                return i
                
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna