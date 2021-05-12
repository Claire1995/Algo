class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        nm = [[0 for _ in range(n)] for _ in range(n)]
        
        for y in range(n):
            for x in range(n):
                nx = n-1-y
                ny = x
                nm[ny][nx] = matrix[y][x]
        print(nm)
                
Solution.rotate(0, [[1,2],[3,4]])

        