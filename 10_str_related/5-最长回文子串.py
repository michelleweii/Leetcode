# 马拉车算法——Manacher 算法 
#
# 现将字符串通过添加特定字符'#'，变成奇数个数。对新字符串使用中心扩展发即可，中心扩展法得到的半径就是子串的长度。
#
# 先转化字符串'35534321'  ---->  '#3#5#5#3#4#3#2#1#'，然后求出以每个元素为中心的最长回文子串的长度。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # manacher 算法
        s = '#' + '#'.join('{}'.format(s)) + '#'
        lens=len(s)
        max_str = ""
        max_length = 0
        for i in range(lens):
            cur_length,cur_str = self.getLength(s,i)
            if cur_length>max_length:
                max_length = cur_length
                max_str = cur_str
        return max_str.replace('#','')

    def getLength(self,s,index):
        length = 0
        string = s[index]
        for i in range(1,index+1):
            # 从index开始的原因是：从当前词开始向两边扩散
            if i+index<len(s) and s[index-i]==s[index+i]:
                length+=1
                string = s[index-i:index+i]
            else:
                break
        return length,string

        """
         # 枚举实现——超时
        max_length=0
        max_string=""
        for i in range(len(s)):
            tmp = ""
            for letter in s[i:len(s)]:
                tmp+=letter
                if tmp==tmp[::-1]:
                    if len(tmp)>max_length:
                        max_length=len(tmp)
                        max_string=tmp
        return max_string
        """



if __name__ == '__main__':
    s = "babad"
    myResult = Solution()
    print(myResult.longestPalindrome(s))