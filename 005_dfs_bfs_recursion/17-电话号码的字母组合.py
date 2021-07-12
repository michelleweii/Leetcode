# 求abc和def的全排列
# 全排列就是回溯, 求最短路径也是DFS
# DFS
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
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



if __name__ == '__main__':
    digits ="23"
    print(Solution().letterCombinations(digits))