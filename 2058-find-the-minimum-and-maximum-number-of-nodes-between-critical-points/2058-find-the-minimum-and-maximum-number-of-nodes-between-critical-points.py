# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        min_dist = float('inf')
        first_crit = -1
        last_crit = -1
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            # A critical point is a local maxima or local minima
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                
                if first_crit == -1:
                    first_crit = idx
                else:
                    # Minimum distance is always between adjacent critical points
                    min_dist = min(min_dist, idx - last_crit)
                
                last_crit = idx
            
            # Step forward
            prev = curr
            curr = curr.next
            idx += 1
            
        # If fewer than 2 critical points were found
        if first_crit == last_crit:
            return [-1, -1]
            
        # Maximum distance is always between the first and last critical points
        return [min_dist, last_crit - first_crit]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna