def recursive(ss, nums, answers):
        if len(nums)==0:
            answers.append(ss)
        else:
            for n in nums:
                nss = ss.copy()
                nss.append(n)
                nnums = nums.copy()
                nnums.remove(n)
                recursive(nss, nnums, answers)

class Solution(object):
    def permute(self, nums):
        answers = []
        for n in nums:
            ss = [n]
            nnums = nums.copy()
            nnums.remove(n)
            recursive(ss, nnums, answers)
        
        return answers


print(Solution.permute(0,[1,2,3]))
        
        