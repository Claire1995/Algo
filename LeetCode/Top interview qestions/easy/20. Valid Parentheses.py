from collections import deque
class Solution(object):
    def isValid(self, s):
        dd = dict()
        dd["("] = ")"
        dd["{"] = "}"
        dd["["] = "]"
        st1 = deque(s)
        st2 = deque()
        
        while st1:
            top1 = st1.pop()
            if top1 in dd.keys(): # 여는 괄호
                if st2:
                    top2 = st2.pop()
                    if dd[top1] != top2:
                        return False
                else:
                    return False
            else: #닫는 괄호
                st2.append(top1)
        if st2:
            return False
        
        return True
    