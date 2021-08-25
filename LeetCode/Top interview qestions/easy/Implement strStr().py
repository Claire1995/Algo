class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        for i, h in enumerate(haystack):
            if len(haystack)-i >= len(needle):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
        