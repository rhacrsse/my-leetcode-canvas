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

    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
       ll = []
       if len(lists) > 0:
           for i in lists:
               ll = ll + self.toList(i) if type(i) != type([]) else i

       ll = list(reversed(sorted(ll)))

       unravell = None

       for i in ll:
           unravell = ListNode(i, unravell)

       return unravell


# UNIT TESTING #
pino = Solution()

# EXAMPLE 1
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
#
lists = [ListNode(1,ListNode(4,ListNode(5))), ListNode(1,ListNode(3,ListNode(4))), ListNode(2,ListNode(6))]
res=pino.mergeKLists(lists)
print(pino.toList(res))

# EXAMPLE 2
#
# Input: lists = []
#
lists = []
res=pino.mergeKLists(lists)
print(pino.toList(res))

# EXAMPLE 3
#
# Input: lists = [[]]
#
lists = [[]]
res=pino.mergeKLists(lists)
print(pino.toList(res))
