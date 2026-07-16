import math
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        max_el = -1
        
        # Step 1: Construct prefix_gcd array
        for num in nums:
            max_el = max(max_el, num)
            prefix_gcd.append(math.gcd(num, max_el))
            
        # Step 2: Sort the array
        prefix_gcd.sort()
        
        # Step 3: Two-pointer pairing
        total_sum = 0
        left, right = 0, n - 1
        
        while left < right:
            total_sum += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return total_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna