# 最短路径
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # python开根号 num_sqrt = n**0.5
        # 对图中所有的点进行预处理，全都没被访问过，设置为false.
        q = []
        q.append((n,0))
        visited = [False for _ in range(n+1)]
        visited[n] = True
        print(q)

        while any(q): # 如果队列不为空的话，执行循环
            num, step = q.pop(0)  # 队列先进先出

            i = 1
            tNum = num-i**2
            while tNum>=0:
                if tNum==0:
                    return step+1

                if not visited[tNum]: # 如果图中的节点没有被访问过
                    q.append((tNum,step+1))
                    visited[tNum]=True
                    print(q)

                i+=1
                tNum = num-i**2

def main():
    n = 12
    myResult = Solution()
    print(myResult.numSquares(n))

if __name__ == '__main__':
    main()
