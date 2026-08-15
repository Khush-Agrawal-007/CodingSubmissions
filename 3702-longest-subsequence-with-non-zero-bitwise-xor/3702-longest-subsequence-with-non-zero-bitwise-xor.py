class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        all_zeros = True
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                all_zeros = False
        
        # If all elements are 0, it's impossible to get a non-zero XOR sum.
        if all_zeros:
            return 0
        
        # If total XOR is non-zero, take the whole array (length N).
        # Otherwise, drop 1 non-zero element to get XOR sum = x != 0 (length N - 1).
        return len(nums) if total_xor != 0 else len(nums) - 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna