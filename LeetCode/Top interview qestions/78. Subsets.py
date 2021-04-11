
            

class Solution(object):
    def subsets(self, nums):
        answers = [[]]

        def recursive(answer, nums):
            if len(nums) != 0:
                print("answer: ", answer)
                
                print("nums: ", nums)
                nnums = nums.copy()
                for i in nums:
                    nanswer = answer.copy()
                    nanswer.append(i)
                    print("i: ", i)
                    print("nanswer: ", nanswer)
                    answers.append(nanswer)
                    nnums.remove(i)
                    print("nnums: ", nnums)
                    recursive(nanswer, nnums)

        nnums = nums.copy()
        for i in nums:
            nnums.remove(i)
            answers.append([i])
            recursive([i], nnums)
        return answers
        
print(Solution.subsets(0, [1, 2, 3]))

