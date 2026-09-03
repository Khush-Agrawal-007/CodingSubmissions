class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        
        # 1. Find the smallest odd number in the array
        for x in nums1:
            if x % 2 != 0 and x < min_odd:
                min_odd = x
                
        # 2. If there are no odd numbers, the array is already all-even
        if min_odd == float('inf'):
            return True
            
        # 3. Check if any even number is smaller than the smallest odd number
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
                
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna