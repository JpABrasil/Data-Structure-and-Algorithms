# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = head
        string = ""
        while temp != None:
            string += str(temp.val)
            temp = temp.next
        binaryInteger = int(string)
        if binaryInteger == 0:
            return binaryInteger

        decimal = 0
        expoente = 0
        for i in reversed(str(binaryInteger)):
            decimal += int(i) *(2**expoente)
            expoente += 1
        return decimal