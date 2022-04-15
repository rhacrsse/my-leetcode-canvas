#!/usr/bin/python3

import math as mt

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

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll = self.toList(head)
        
        half = mt.floor(len(ll)/2) if len(ll) % 2 != 0 else round(len(ll)/2)

        ll = list(reversed(ll[half:]))

        unravell = None

        for i in ll:
            unravell = ListNode(i, unravell)

        return unravell
