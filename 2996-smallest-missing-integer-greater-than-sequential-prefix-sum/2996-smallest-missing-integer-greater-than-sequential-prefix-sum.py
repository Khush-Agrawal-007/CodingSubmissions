class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                # Break as soon as the sequence is no longer sequential
                break
                
        # Step 2: Use a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: Increment the sum until it's no longer in the array
        while prefix_sum in num_set:
            prefix_sum += 1
            
        return prefix_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna