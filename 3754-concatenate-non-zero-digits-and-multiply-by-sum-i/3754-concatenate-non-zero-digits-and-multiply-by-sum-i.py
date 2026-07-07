class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Process each digit: filter out zeros, collect digits
        digits = [int(c) for c in str(n) if c != '0']
        # If all digits were zero, return 0
        if not digits: 
            return 0
        # Concatenate digits as string -> int
        concat_num = int(''.join(str(d) for d in digits))
        # Sum of non-zero digits
        sum_digits = sum(digits)
        # Multiply and return
        return concat_num * sum_digits

        # Time Complexity: O(d) where d = number of digits in n
        # Space Complexity: O(d) for storing digits list
        # Optimal approach - this is the most efficient possible

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna