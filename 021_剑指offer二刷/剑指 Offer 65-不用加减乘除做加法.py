"""
easy 位运算
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
2021-07-21
"""
class Solution:
    def add(self, a: int, b: int) -> int:


        # 超出时间限制
        while b:
            sum = a^b # 求和
            carry  = (a & b) << 1  # 进位
            a = sum
            b = carry
        return a

if __name__ == '__main__':
    a = 1
    b = 1
    print(Solution().add(a, b))