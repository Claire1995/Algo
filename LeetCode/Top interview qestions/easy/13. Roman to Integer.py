class Solution(object):
    def romanToInt(self, s):
        d = dict()
        d['I'] = 1
        d['IV'] = 4
        d['V'] = 5
        d['IX'] = 9
        
        d['X'] = 10
        d['XL'] = 40
        d['L'] = 50
        d['XC'] = 90
        
        d['C'] = 100
        d['CD'] = 400
        d['D'] = 500
        d['CM'] = 900
        
        d['M'] = 1000
        
        answer = 0
        sp = False
        for idx, n in enumerate(s):
            if sp:
                sp = False
                continue
            print(n)
            if (n == 'I' or n == 'X' or n == 'C') and idx<len(s)-1:
                if n+s[idx+1] in d.keys():
                    sp=True
                    ss = n+s[idx+1]
                    answer += d[ss]
                else:
                    answer += d[n]
            else:
                answer += d[n]
        
        return answer