class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Generate all possible sequential numbers (length 2-9, starting digits 1-8 for 2-digit)
        res = []
        for length in range(2, 10):  # length of sequential digits
            for start in range(1, 10 - length + 1):
                # Build number like 12, 23, ..., 123, 234, etc.
                digits = [str(start + i) for i in range(length)]
                num = int(''.join(digits))
                res.append(num)
        
        # Sort all generated numbers
        res.sort()
        
        # Filter by [low, high] range using list comprehension
        return [x for x in res if low <= x <= high]

        # Time Complexity: O(1) - fixed 36 possible sequential numbers
        # Space Complexity: O(1) - stores at most 36 numbers
        # Optimal: This is the most efficient approach for this problem.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna