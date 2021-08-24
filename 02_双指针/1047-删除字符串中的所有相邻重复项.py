"""
easy
双指针同向
思路：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/solution/tong-xiang-shuang-zhi-zhen-bian-xing-by-hr5zk/
"""
class Solution:
    def removeDuplicates(self, s):
        s = list(s)
        left, right = -1, 0
        n = len(s)
        while right < n:
            if left==-1 or s[left]!=s[right]:
                left += 1
                s[left] = s[right]
                right += 1
            else:

                right += 1
                left -= 1
        return "".join(s[:left+1])

    """ 栈
    stk = []
    n = len(s)
    i = 0
    while i < n:
        cur = s[i]
        i += 1
        if stk and stk[-1]==cur:
            stk.pop()
        else:
            stk.append(cur)
    return "".join(stk)
    """

if __name__ == '__main__':
    s = "abbaca"
    ans = Solution()
    print(ans.removeDuplicates(s)) # "ca"