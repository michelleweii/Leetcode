"""
middle 超级经典
栈
思路：
- 处理运算符优先级的问题。easy-扫描2遍:第一遍，将所有的乘除法干掉；第二遍，再计算加减法;
- 双栈用栈来做：
   - 第一个栈存储运算符，第二个栈存储数字；
   - 枚举，运算符push进栈；如果是数字，将连续的数字找出来，
        如果栈顶是乘除，则直接计算，计算后再压入栈顶，op栈弹掉；
        现在只需要计算加减法 从左向右计算就可以
    - 最后栈顶是答案。

- 单栈做法：https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-bu-dai-gua-hao-shuang-br4d5/
"""
class Solution:
    def calculate(self, s):
        n = len(s)
        stk = []
        pre_sign = '+' # 用 pre_op 记录上一个运算符的方法
        num = 0
        # 入栈的过程中把乘除法的中间结果算出来
        for i in range(n):
            # 遍历123，是一个一个枚举，要累加才是最终的数字
            if s[i]!=' ' and s[i].isdigit():
                num = num*10 + ord(s[i]) - ord('0')

            if i==n-1 or s[i] in '+-*/':
                if pre_sign == '+':
                    stk.append(num)
                elif pre_sign == '-':
                    stk.append(-num)
                elif pre_sign == '*':
                    stk.append(stk.pop()*num)
                else:
                    # 这里需要注意一些 -3/2=-1 不是(-3)//2=-2 所以不能是//
                    stk.append(int(stk.pop()/num))
                pre_sign = s[i]
                num = 0
        return sum(stk)

if __name__ == '__main__':
    s = "31+2*2"
    print(Solution().calculate(s))