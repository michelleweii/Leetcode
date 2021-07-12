"""
middle
双指针同向
思路：遍历所有座位 seats，找出每个空位左边最近的人和右边最近的人，更新当前空位到最近的人的距离。
使用 prev 记录 i 最左边第一个有人的位置，future 记录 i 最右边第一个有人的位置。
座位 i 到最近的人的距离为 min(i - prev, future - i)。
另外有一种特殊情况，如果座位 i 左边没有人，则认为到左边第一个人的距离是无限大，右边同理。

链接：https://leetcode-cn.com/problems/maximize-distance-to-closest-person/solution/dao-zui-jin-de-ren-de-zui-da-ju-chi-by-leetcode/
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        # 左右指针指的是有人的位置。
        # 遍历的是无人的位置。
        people = (i for i, seat in enumerate(seats) if seat)
        # print(people) # <generator object Solution.maxDistToClosest.<locals>.<genexpr> at 0x000001C8E3F2AC48>
        prev, future = None, next(people)
        ans = 0
        for i, seat in enumerate(seats):
            if seat: # 如果该位置有人
                prev = i
            # 找该空位下一个有人的位置
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
"""
        ans1,ans2,ans3 = 0,0,0
        # seats_str = ''.join([str(i) for i in seats]).split('1') # ['', '000']
        # print(seats_str)
        # seats_str.remove('')  # ['000']
        seats_str = ''.join(map(str, seats)).split('1')
        # 这种没有空格 # seats = ''.join(map(str, seats)).split('1')  # ['000']
        # 在中间
        seats_str = list(map(len, seats_str))
        ans3 = (max(seats_str) + 1) // 2
        # print("ans3",ans3)
        # print(seats_str) # [0, 3]
        # # 在首尾
        # print(seats) # [1, 1, 0, 0, 0]
        # print(seats[:-1]) # [1, 1, 0, 0]
        # print(seats[::-1]) # [0, 0, 0, 1, 1]
        if seats[0] == 0:
            ans1 = seats.index(1)  # 数字1的下标是多少？
            # print("ans1",ans1)
        if seats[len(seats)-1] == 0:
            ans2 = seats[::-1].index(1)
            # print("ans2",ans2)
        return max(ans1,ans2,ans3)
"""

if __name__ == '__main__':
    # seats = [1,0,0,0]#
    seats = [1,1,0,0,0,1,0]
    # seats = [1,1,0,0,0]
    myansult = Solution()
    print(myansult.maxDistToClosest(seats))
