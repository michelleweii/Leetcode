"""
1. 如果首尾是1的情况，那么只能坐在两个1之间；

2. 如果首尾是0的情况，那么可以坐在0之前或者0之后。

"""

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # input:  seats = [1,1,0,0,0]
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



def main():
    seats = [1,1,0,0,0,1,0]
    # seats = [1,1,0,0,0]
    myResult = Solution()
    print(myResult.maxDistToClosest(seats))

if __name__ == '__main__':
    main()