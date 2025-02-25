# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head):
        p1 = head
        p2 = head
        og = head

        while (p2.next is not None):
            p2 = p2.next.next
            temp = p1
            p1 = p1.next

        temp.next = p1.next
        return og



def main():
    candies = [1,3,4,7,1,2,6]
    sol_obj = Solution()
    result = sol_obj.deleteMiddle(candies)
    print(result)


if __name__ == '__main__':
    main()
