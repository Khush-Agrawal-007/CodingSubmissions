class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Find the last occurrence index of each character
        last_occ = {char: i for i, char in enumerate(s)}
        
        stack = []
        visited = set()
        
        for i, char in enumerate(s):
            # If the character is already in our path, we don't need it again
            if char in visited:
                continue
                
            # Pop characters from the stack if:
            # 1. The stack isn't empty
            # 2. The top of the stack is larger than the current char (greedily seeking smaller chars)
            # 3. The top of the stack occurs again later in the string
            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)
                
            stack.append(char)
            visited.add(char)
            
        return "".join(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna