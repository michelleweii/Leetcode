"""
middle 二分查找
"""
# https://leetcode-cn.com/problems/heaters/solution/er-fen-cha-zhao-de-jie-fa-by-li-xian-sen/
# 右边 >=item的最小数（可能不存在，用哨兵）
# 左边 <=item的最大数（可能不存在，用哨兵）

# 对任何一个房间，要不从他前面的取暖器采暖，要不从他后面的取暖。 把这个思考清楚了，按照这个想法去实现代码很简单。
import bisect
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        res = 0
        # for house in houses:
        #     loc = bisect.bisect_left(heaters, house)
        #     print("loc", loc)
        #     res = max(res, min(house - heaters[loc - 1], heaters[loc] - house))
        # return res

        # print(heaters) # [-inf, 2, inf]
        for house in houses:
            l, r = 0, len(heaters)-1
            # 在heaters中找到目标元素house第一次出现的位置
            while(l<r):
                mid = (l+r)//2
                if heaters[mid]>=house:r=mid  # 这里卡住
                else:l=mid+1

            # heaters[left] <= house:
            # 若该加热器的坐标值小于house ，说明该加热器的坐标与house之间没有别的加热器

            # else:
            # 说明house介于left和left-1之间，房屋到加热器的最短距离就是left和
            # left-1处加热器与house差值的最小值.
            res = max(res, min(house-heaters[l-1], heaters[l]-house)) #将距离房子最近的供暖器距离纳入统计
        return res


if __name__ == '__main__':
    # houses = [1,2,3] heaters = [2] # 1
    houses = [1, 2, 3, 4]
    heaters = [1, 4] # 1
    res = Solution()
    print(res.findRadius(houses, heaters))