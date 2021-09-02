# 贪心算法
class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g) # 需求
        s = sorted(s)  # 糖果
        child = 0 # 已满足几个孩子
        cookie = 0 # 尝试了几个糖果
        while cookie < len(s) and child < len(g):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


    # 超出时间限制，自己写的
    def findContentChildren1(self, g, s):
        g = sorted(g) # 需求
        s = sorted(s)  # 糖果
        cnt = 0
        flag = []
        for index_g,val_g in enumerate(g):
            for index_s, val_s in enumerate(s):
                if val_s >= val_g and index_s not in flag:
                    cnt += 1
                    flag.append(index_s)
                    break
        return cnt





if __name__ == '__main__':
    g = [1,2]
    s = [1,2,3]
    print(Solution().findContentChildren(g,s))