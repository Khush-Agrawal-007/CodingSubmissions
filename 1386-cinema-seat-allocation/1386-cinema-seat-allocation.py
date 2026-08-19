from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map row number -> set of reserved seats in seats 2..9
        row_reserved = defaultdict(set)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                row_reserved[r].add(c)
        
        # Any row without reservations can fit 2 families
        ans = (n - len(row_reserved)) * 2
        
        # Check rows that have reservations
        for seats in row_reserved.values():
            left = not (seats & {2, 3, 4, 5})
            right = not (seats & {6, 7, 8, 9})
            middle = not (seats & {4, 5, 6, 7})
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna