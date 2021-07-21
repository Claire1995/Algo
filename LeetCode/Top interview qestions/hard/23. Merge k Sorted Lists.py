import heapq
class Solution(object):
    def mergeKLists(self, lists):
        hp = []
        answer = []
        for l in lists:
            temp = l
            while temp:
                # print(temp)
                heapq.heappush(hp, temp.val*-1)
                temp = temp.next
        
        node = False
        while len(hp)>0:
            temp = heapq.heappop(hp) *-1
            if node:    
                node = ListNode(temp, node)
            else:
                node = ListNode(temp)
            # print('val: ', node.val)
            # print('val: ', node.next)
        
        if node == False:
            return
        return node
        