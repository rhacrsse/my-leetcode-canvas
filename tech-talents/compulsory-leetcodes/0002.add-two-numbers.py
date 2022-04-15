#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def toList(self, head: [ListNode]) -> []:
        s = []
        while (head.next != None):
            s.append(head.val)
            head = head.next
        s.append(head.val)
        return s

    def temp(self, l1: [ListNode], l2: [ListNode], carry: int) -> [ListNode]:
        if l1 == None and l2 == None:
            return ListNode(carry) if carry > 0 else None

        if l1 == None:
            tot = carry + l2.val
            if tot >= 10:
                tot = tot - 10
                carry = 1
            else:
                carry = 0

            return ListNode(tot, self.temp(None, l2.next, carry))

        if l2 == None:
            tot = carry + l1.val
            if tot >= 10:
                tot = tot - 10
                carry = 1
            else:
                carry = 0

            return ListNode(tot, self.temp(l1.next, None, carry))

        tot = carry + l1.val + l2.val
        if tot >= 10:
            tot = tot - 10
            carry = 1
        else:
            carry = 0

        return ListNode(tot, self.temp(l1.next, l2.next, carry))

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        return self.temp(l1,l2,0)

# UNIT TESTING #
pino = Solution()

l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))
res=pino.addTwoNumbers(l1,l2)
print(pino.toList(res))

l1 = ListNode(0)
l2 = ListNode(0)
res=pino.addTwoNumbers(l1,l2)
print(pino.toList(res))

l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))
res=pino.addTwoNumbers(l1,l2)
print(pino.toList(res))
