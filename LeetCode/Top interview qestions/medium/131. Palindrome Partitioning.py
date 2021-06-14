class Solution(object):
    def __init__(self):
        # store palindrome => key: partition, val: output of this partition
        self.p = dict()

    def isPalindrome(self, s):
        print("isPalindrome: ", s)
        if len(s)==0:
            print("len 0")
            return True
        elif s in self.p:
            print("hist")
            return self.p[s]
        else:
            for i in range(int(len(s)/2)):
                if s[i] != s[len(s)-1-i]:
                    print("False")
                    return False
            print("True")
            return True

    def recursive(self, s):
        result = []
        #1. 나눈다
        if len(s)==1:
            result.append([s])
            return result

        for i in range(1, len(s)):
            print("i: ", i)
            s1 = s[0:i]
            s2 = s[i:]
            print("s1: ", s1)
            print("s2: ", s2)
            # 2. 둘 다 p인가?
            isp1 = Solution.isPalindrome(self, s1)
            isp2 = Solution.isPalindrome(self, s2)
            print("isp1 : ", isp1)
            print("isp2 : ", isp2)
            if isp1 and isp2 and [s1, s2] not in result:
                result.append([s1, s2])

            # 3. 길이가 크면 더 나눠본다
            r1 = []
            r2 = []
            if len(s1)>0:
                if type(isp1) == bool:
                    r1 = Solution.recursive(self, s1)
                else:
                    r1 = isp1
                print("r1: ", r1)
                
            if len(s2)>0:
                if type(isp2) == bool:
                    r2 = Solution.recursive(self, s2)
                    if len(r2)>0:
                        self.p[s2] = r2
                    else: 
                        self.p[s2] = [s2]
                else:
                    r2 = isp2
                print("r2: ", r2)
            
            if len(r1)> 0 and len(r2)> 0:
                for i in r1:
                    for j in r2:
                        temp = []
                        for a in i:
                            temp.append(a)
                        for a in j:
                            temp.append(a)
                        if temp not in result:
                            result.append(temp)
                        

        return result
                

    def partition(self, s):
        result = Solution.recursive(self, s)
        if Solution.isPalindrome(self, s) and [s] not in result:
            result.append([s])
        print(self.p.keys())
        return result


print(Solution.partition(Solution(), "abbab"))
        
        
        

