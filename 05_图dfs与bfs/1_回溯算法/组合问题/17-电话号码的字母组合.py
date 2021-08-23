"""
middle
求abc和def的全排列（这类不需要start_index）
全排列就是回溯, 求最短路径也是DFS
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.md
链接里的图很重要，有助于理解
"""
class Solution(object):
    def __init__(self):
        self.res = []
        self.path = ""
        self.hash_map = {'0': "", '1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits):
        if not digits:return self.res
        self.dfs(digits,0) # 0是从digits的第0位开始
        return self.res

    def dfs(self,digits,index):
        # 定义出口
        if len(self.path) == len(digits):
            self.res.append(self.path)
            return
        letters = self.hash_map[digits[index]]  # 取出数字对应的字符集
        for i in range(len(letters)): # 控制树的第2层
            self.path += letters[i]
            self.dfs(digits,index+1) # digits的下一个字符串
            self.path = self.path[:-1] #  回溯

    """
    def letterCombinations(self, digits):
        # 存储结果的数组
        res = []
        inputstr = []
        if len(digits) == 0:
            return res
        hash_map = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        for i in digits:
            inputstr.append(hash_map[int(i)])
        # print(inputstr) # ['abc', 'def']
        # 闭包
        def dfs(cur_str,i,res):
            if len(cur_str)==len(inputstr): # abc def ghi
                res.append(cur_str)
                return
            for count in range(len(inputstr[i])): # abc
                dfs(cur_str+inputstr[i][count],i+1,res)

        dfs("",0,res)
        return res
    """



if __name__ == '__main__':
    digits ="23"
    print(digits[:-1]) #2
    print(Solution().letterCombinations(digits))