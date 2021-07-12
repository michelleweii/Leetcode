class solution(object):
    def search(self, nums, target) -> bool:
        if not nums:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            if nums[low] == nums[mid]:
                low += 1
            elif nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid
                else:
                    high = mid - 1
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(solution().search(nums, target))
