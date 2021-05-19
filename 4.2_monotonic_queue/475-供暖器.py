# 二分查找
# 对每一个房屋进行二分，找到左边、右边第一个暖气的位置
# 右边 >=item的最小数（可能不存在，用哨兵）
# 左边 <=item的最大数（可能不存在，用哨兵）

# 对任何一个房间，要不从他前面的取暖器采暖，要不从他后面的取暖。 把这个思考清楚了，按照这个想法去实现代码很简单。
import bisect
class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        res = 0
        for house in houses:
            loc = bisect.bisect_left(heaters, house)
            print("loc", loc)
            res = max(res, min(house - heaters[loc - 1], heaters[loc] - house))
        return res
        # heaters.sort()
        # heaters = [float("-inf")] + heaters + [float("inf")]
        # res = 0
        # # print(heaters) # [-inf, 2, inf]
        # for house in houses:
        #     l,r=0,len(houses)-1
        #     while(l<r):
        #         mid = (l+r)//2
        #         if heaters[mid]<house:r=mid
        #         else:l=mid+1
        #
        #     # 暖气在房子右边
        #     dist_r =  heaters[l]-house
        #     # 暖气在房子左边
        #     dist_l = house-heaters[l-1]
        # #     loc = bisect.bisect_left(heaters, house)
        #     res = max(res, min(dist_l, dist_r)) #将距离房子最近的供暖器距离纳入统计
        # return res


if __name__ == '__main__':
    houses = [1,2,3]
    heaters = [2]
    res = Solution()
    print(res.findRadius(houses, heaters))