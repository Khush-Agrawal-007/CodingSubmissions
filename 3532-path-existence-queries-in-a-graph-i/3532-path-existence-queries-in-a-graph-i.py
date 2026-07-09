class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # g tracks the connected component ID of each node
        g = [0] * n
        component_id = 0
        
        for i in range(1, n):
            # If the gap is too large, the component breaks
            if nums[i] - nums[i - 1] > maxDiff:
                component_id += 1
            g[i] = component_id
            
        # Answer each query in O(1) time
        return [g[u] == g[v] for u, v in queries]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna