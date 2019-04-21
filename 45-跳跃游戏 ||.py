class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        广度优先搜索，时间复杂度O(N)，注意不要搜索重复的节点
        """
        l = len(nums)
        if l == 1: return 0

        from collections import deque
        q = deque()
        res = 0
        visited = [False for i in range(l)]
        q.append(0)
        visited[0] = True
        while q:
            for j in range(len(q)):
                node = q.popleft()
                for i in range(nums[node], 0, -1):  # 从最大开始找有助于加快速度
                    new_index = node + i
                    if new_index >= l - 1:
                        return res + 1
                    if not visited[new_index]:
                        visited[new_index] = True
                        q.append(new_index)
            res += 1


            