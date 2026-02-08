# LeetCode 2: Add Two Numbers
# Time: O(max(m, n))
# Space: O(max(m, n))

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            s = x + y + carry
            carry = s // 10

            cur.next = ListNode(s % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# Helper functions for local testing
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))


if __name__ == "__main__":
    sol = Solution()
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    print_list(res)  # 7 -> 0 -> 8
