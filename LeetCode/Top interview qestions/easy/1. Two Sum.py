class Solution(object):
    def twoSum(self, nums, target):
        dd = dict()
        for idx, n in enumerate(nums):
            if n in dd.keys():
                dd[n].append(idx)
            else:
                dd[n] = [idx]
        
            
        for idx, n in enumerate(nums):
            y = target - n
            if y in dd.keys():
                arr = dd[y]
                print(arr)
                for i, m in enumerate(arr):
                    if m != idx:
                        return [m, idx]
                
            