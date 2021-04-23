class Solution(object):
    def groupAnagrams(self, strs):
        output = []
        strs2 = []
        for s in strs:
            ss = sorted(s)
            new = True
            for i in range(len(output)):
                if output[i][0] == s or strs2[i] == ss:
                    output[i].append(s)
                    new = False
                    break
            if new == True:
                output.append([s])
                strs2.append(sorted(s))
        return output

#   배운점#
#   some_list.sort() -- iterable 본체정렬 vs sorted(string, reverse=True)
                    
        