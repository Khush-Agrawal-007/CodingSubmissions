class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Create a sorted list of unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a hash map mapping each value to its rank
        # Enumerate starts counting at 1 (rank 1)
        rank_map = {val: rank for rank, val in enumerate(sorted_unique, 1)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna