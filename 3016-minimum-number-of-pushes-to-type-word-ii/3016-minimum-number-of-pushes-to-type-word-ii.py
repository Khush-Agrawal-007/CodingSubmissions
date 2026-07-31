class Solution:
    def minimumPushes(self, word: str) -> int:
        from collections import Counter
        
        # 1. Count the frequency of each character
        freq = Counter(word)
        
        # 2. Sort the frequencies in descending order
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        
        # 3. Calculate total pushes using the greedy approach
        for i, count in enumerate(sorted_freq):
            # i // 8 determines the "layer". 
            # First 8 letters -> layer 0 (1 push)
            # Next 8 letters -> layer 1 (2 pushes), etc.
            pushes_needed = (i // 8) + 1
            total_pushes += count * pushes_needed
            
        return total_pushes

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna