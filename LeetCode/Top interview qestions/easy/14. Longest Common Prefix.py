class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ""
        strs.sort()
        prefix = strs[0]
        for s in strs:
            if not s.startswith( prefix ) :
                n  = min(len(prefix), len(s))
                nxt = ""
                for i in range(n):
                    if prefix[i] == s[i]:
                        nxt += prefix[i]
                    else:
                        break
                if not nxt:
                    return nxt
                else:
                    prefix = nxt
        return prefix