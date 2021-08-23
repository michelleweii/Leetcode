class Solution(object):
    def search(self, nums, target):
        # 需找到自增区间、旋转区间
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid

            elif target<nums[mid]:
                if nums[low]<nums[mid]:
                    if target >= nums[low]:
                        high = mid-1
                    else:
                        low = mid+1
                elif nums[low] > nums[mid]:
                    high = mid-1
                elif nums[low]==nums[mid]:
                    low = mid+1

            elif target>nums[mid]:
                if nums[low] < nums[mid]:
                    low = mid+1
                elif nums[low] > nums[mid]:
                    if target>=nums[low]:
                        high = mid-1
                    else:
                        low = mid+1
                elif nums[low]==nums[mid]:
                    low = mid+1

        return -1



if __name__ == '__main__':
    nums = [5,1,2,3,4]
    target = 1
    print(Solution().search(nums,target))
