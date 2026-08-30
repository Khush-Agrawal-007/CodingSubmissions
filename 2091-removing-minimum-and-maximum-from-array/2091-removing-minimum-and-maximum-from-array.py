class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # 1. Find indices of the minimum and maximum values
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        
        # 2. Ensure i is the smaller index and j is the larger index
        if i > j:
            i, j = j, i
            
        # 3. Calculate the cost of the three possible strategies
        front_deletions = j + 1          # Remove everything from the front up to j
        back_deletions = n - i           # Remove everything from the back down to i
        both_ends = (i + 1) + (n - j)    # Remove i from the front and j from the back
        
        # 4. Return the most efficient route
        return min(front_deletions, back_deletions, both_ends)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna