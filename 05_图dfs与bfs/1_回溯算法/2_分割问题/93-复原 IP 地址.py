"""
# middle 2021/08/24
回溯法-分割问题-有startindex,
"""
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def restoreIpAddresses(self, s):
        if not s:return self.res
        if len(s)>3*4:return self.res
        self.dfs(s,0)
        return self.res

    def dfs(self,s,start_index):
        # 定义出口
        # start_index==len(s) 很重要，说明整个字符串遍历结束了
        if len(self.path)==4 and start_index==len(s):
            self.res.append(".".join(self.path))
            return

        # for循环遍历树层，一个ip中的每个部分，不超过3个数字，所以min+4
        for i in range(start_index,min(start_index+4,len(s))):
            p = s[start_index:i+1]
            # 定义剪枝
            # 每个整数位于 0 到 255 之间组成
            if int(p)>255 or int(p)<0:
                continue
            # ip不能含有前导 0
            if len(p)>1 and p[0]=='0':continue
            self.path.append(p)
            # 树枝递归
            self.dfs(s,i+1)
            self.path.pop()

if __name__ == '__main__':
    # s = "25525511135"
    # ["255.255.11.135","255.255.111.35"]
    # s = "0000"
    s = "010010"
    print(Solution().restoreIpAddresses(s))