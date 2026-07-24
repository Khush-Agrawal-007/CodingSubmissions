class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Step 1: Extract unique values
        S = list(set(nums))
        
        # Step 2: Compute all unique pair XORs
        pairs = {x ^ y for i, x in enumerate(S) for y in S[i:]}
        
        # Step 3: Compute all unique triplet XORs
        triplets = {p ^ z for p in pairs for z in S}
        
        return len(triplets)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna