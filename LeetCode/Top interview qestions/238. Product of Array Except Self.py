class Solution(object):
    def productExceptSelf(self, nums):
        answers = []
        
        total = 1
        zeros = []

        for i in range(len(nums)):
            n = nums[i]
            if n!=0:
                total *= n  
            else:
                zeros.append(i)
        
        for i in range(len(nums)):
            if nums[i]!=0:
                answer = total/nums[i]
                if zeros:
                    answer = 0
            else:
                answer = total
                if len(zeros)>1:
                    answer = 0
            answers.append(answer)
            
        return print(answers)

Solution.productExceptSelf(0, [0, 1, 2, 3, 0, 4])
        