
class Solution(object):
    def topKFrequent(self, nums, k):
        answers = []
        fList = [[] for _ in range(len(nums)+1)] 
        for n in nums:
            inFlist = False
            for f in fList:
                if n in f:
                    print(n)
                    print(fList)
                    idx = fList.index(f)
                    f.remove(n)
                    fList[idx+1].append(n)
                    print(fList)
                    print("====")
                    inFlist = True
                    break
            if inFlist == False:
                fList[1].append(n)
                    
        print(fList)
        for i in range(len(fList)-1, 0, -1):
            if k!=0:
                if len(fList[i])==0:
                    continue
                else:
                    for f in fList[i]:
                        if k==0:
                            return answers
                        answers.append(f)
                        k -= 1
            else:
                break
        return answers

print(Solution.topKFrequent(0, [5,3,1,1,1,3,73,1], 1))