class Solution(object):
    def halvesAreAlike(self, s):
        l = len(s)
        a = s[0:int(l/2)]
        b = s[int():]
        print(a)
        print(b)
        vowels =  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cntA = 0
        cntB = 0
        for aa in a:
            print(aa)
            if aa in vowels:
                cntA += 1
        
        for bb in b:
            print(bb)
            if bb in vowels:
                cntB += 1

        if cntA == cntB:
            return True
        else:
            return False

print(Solution.halvesAreAlike(1, "book"))