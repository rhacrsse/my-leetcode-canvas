#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def toList(self, head: [ListNode]) -> []:
        s = []
        if head == None:
            return s
        while (head.next != None):
            s.append(head.val)
            head = head.next
        s.append(head.val)
        return s

    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        ll = self.toList(head)

        ll = list(reversed(ll))
        ll.pop(n-1)

        unravell = None

        for i in ll:
            unravell = ListNode(i, unravell)

        return unravell



# UNIT TESTING #
pino = Solution()

# EXAMPLE 1
#
# Input: head = [1,2,3,4,5], n = 2 
#
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
n = 2
res=pino.removeNthFromEnd(head,n)
print(pino.toList(res))


# EXAMPLE 2
#
# Input: head = [1], n = 1 
#
head = ListNode(1)
n = 1
res=pino.removeNthFromEnd(head,n)
print(pino.toList(res))

# EXAMPLE 3
#
# Input: head = [1,2], n = 1 
#
head = ListNode(1,ListNode(2))
n = 1
res=pino.removeNthFromEnd(head,n)
print(pino.toList(res))

# EXAMPLE 4
#
# Input: head = [3,7,9,3,5,8,0], n = 1 
#
head = ListNode(3,ListNode(7,ListNode(9,ListNode(3,ListNode(5,ListNode(8,ListNode(0)))))))
n = 1
res=pino.removeNthFromEnd(head,n)
print(pino.toList(res))
