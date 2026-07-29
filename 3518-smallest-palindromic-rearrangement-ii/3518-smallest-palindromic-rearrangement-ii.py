import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        
        half = [0] * 26
        mid = ""
        total_len = 0
        
        # 1. Build character frequencies for the left half
        for i in range(26):
            char = chr(i + ord('a'))
            if freq[char] % 2 != 0:
                mid += char
            
            # Halve the frequencies for the left side of the palindrome
            half[i] = freq[char] // 2
            total_len += half[i]
            
        # Helper to calculate permutations of the remaining left half characters
        def count_permutations():
            ways = 1
            rem = total_len
            for count in half:
                if count > 0:
                    ways *= math.comb(rem, count)
                    rem -= count
                    # Cap ways at 10^6 + 1 to prevent large integer operations
                    if ways > 10**6:
                        return 10**6 + 1
            return ways
            
        # If total possible permutations are less than k, return empty string
        if count_permutations() < k:
            return ""
            
        left_half = []
        original_len = total_len
        
        # 2. Greedily determine each character of the left half
        for _ in range(original_len):
            for i in range(26):
                if half[i] == 0:
                    continue
                
                # Tentatively place this character
                half[i] -= 1
                total_len -= 1
                
                ways = count_permutations()
                
                if ways >= k:
                    # We have enough ways to reach k. Character confirmed!
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    # Not enough ways. Backtrack, decrease k, and try the next character.
                    k -= ways
                    half[i] += 1
                    total_len += 1
                    
        # 3. Assemble the final palindrome
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna