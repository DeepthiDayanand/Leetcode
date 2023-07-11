# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        #slow is now the midpoint, reverse the linked list from the midpoint
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
        
        
        
        
        
        
        
        
        
        
        
        
#         ------Method 1-------
#         <- Put the values of the linked list into an array and then use two pointers on the array ->
#         nums = []
        
#         while head:
#             nums.append(head.val)
#             head = head.next
            
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             if nums[l] != nums[r]:
#                 return False
#             l += 1
#             r -= 1
            
#         return True

        

