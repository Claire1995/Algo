import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        # heap ~ sth like priorityQueue
        arr = []
        for m in matrix:
            for num in m:
                heapq.heappush(arr, num)
        
        for _ in range(k):
            temp = heapq.heappop(arr)
        
        return temp

        # divide and conquer
        # https://jackjeong.tistory.com/73 참고
        

# binary search??
# 이진 탐색 알고리즘(binary search algorithm)은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.
# 정렬된 리스트의 중간 값을 임의로 선택해, 그 값과 찾고자 하는 값의 대소를 비교하는 방식이다.
# 반복문 혹은 재귀용법을 사용해서 구현할 수 있다.

# 검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만, 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.

Solution.kthSmallest(0, [[1,5,9],[10,11,13],[12,13,15]], 8)