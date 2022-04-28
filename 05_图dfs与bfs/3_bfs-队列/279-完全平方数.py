"""
middle 2022-03-17 最短路径BFS遍历/DP
BFS的做法，比较巧妙。每一次是原数字减去了一个平方数，直到出现第一个0，此时走过的层数就是最小数量，即为答案
https://leetcode-cn.com/problems/perfect-squares/solution/python3zui-ji-chu-de-bfstao-lu-dai-ma-gua-he-ru-me/
# 假设数字为7，就是下面这个树，可以等价最短路径(7-1^2,7-2^2)
        7
       / \
      6   3
    / \    \
   5   2    2
  / \   \    \
 4   1   1    1
"""
class Solution(object):
    def numSquares(self, n):
        # python开根号 num_sqrt = n**0.5
        # 对图中所有的点进行预处理，全都没被访问过，设置为false.
        q = []
        q.append((n,0)) # (value,step)
        visited = [False for _ in range(n+1)]
        visited[n] = True
        while q: # 如果队列不为空的话，执行循环
            num, step = q.pop(0)  # 队列先进先出
            i = 1
            target = num-i**2
            while target>=0:
                if target==0:
                    return step+1
                if not visited[target]: # 如果图中的节点没有被访问过
                    q.append((target,step+1))
                    visited[target]=True

                i+=1
                target = num-i**2
        return -1
# 【学习1】
#         while deq:
#             number,step=deq.popleft()
#             targets=[number-i*i for i in range(1,int(number**0.5)+1)]
#             for target in targets:
#                 if target==0:return step+1
#                 if target not in visited:
#                     deq.append((target,step+1))
#                     visited.add(target)
#         return 0

# 【学习2】
#         #存储在n范围内的完全平方数
#         squares = [i*i for i in range(int(n**0.5)+1)]
#         visited = set() #存储之前出现过的结果，为了剪枝
#         queue = [n]
#         count = 0 #当前层数
#         while queue:
#             #这里类似于二叉树的层序遍历
#             for _ in range(len(queue)):
#                 curr = queue.pop(0)
#                 #当前节点值为0，返回结果
#                 if curr == 0:
#                     return count
#
#                 for s in squares:
#                     res = curr - s
#                     if res >= 0 and res not in visited:
#                         queue.append(res)
#                         visited.add(res)
#             count += 1
if __name__ == '__main__':
    n = 7
    print(Solution().numSquares(n))