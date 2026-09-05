class Solution:

  def firstStableIndex(self, nums: list[int], k: int) -> int:
    n = len(nums)
    right = [nums[-1]] * n

    # Step 1: Precompute suffix minimums
    for i in range(n - 2, -1, -1):
      right[i] = min(right[i + 1], nums[i])

    # Step 2: Traverse with a running prefix maximum
    left = 0
    for i, x in enumerate(nums):
      left = max(left, x)
      if left - right[i] <= k:
        return i

    return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna