# 贪心
# 前一个数字比后一个数字大，则删掉前面的数字
class Solution(object):
    def removeKdigits(self, num, k):
        if k==len(num):
            return '0'
        stack = []
        for i in num:
            while stack and k and i<stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
      # 12345,k=3的时候
        while k:
            stack.pop()
            k-=1
        if stack is None:
            return '0'
        # 处理 10200,k=1的时候
        print(stack)
        print("".join(stack).lstrip('0')) #
        # ['0', '2', '0', '0']
        # 200
        return "".join(stack).lstrip('0') or "0"


if __name__ == '__main__':
    num = "10"
    k = 1
    print(Solution().removeKdigits(num,k))