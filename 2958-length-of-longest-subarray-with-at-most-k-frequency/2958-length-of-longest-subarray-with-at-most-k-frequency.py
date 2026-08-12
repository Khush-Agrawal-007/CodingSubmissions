class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            
            # Shrink window from the left until the frequency condition is satisfied
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna