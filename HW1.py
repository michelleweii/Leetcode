
# 题目大概是有一串1-9组成的列表，数字代表优先级，数字越大优先级越高。从第一个数字开始判断，
# 如果列表中没有优先级比它还高的数字，就执行它，如果后边有比它优先级还要高的数字，
# 就把第一个数字放到列表尾端，依次往下判断，直至所有数据都被执行。然后题目要求输出这串列表中每个数字执行的顺序。
# ---------------------

def numSorted_2(nums):
    # nums = [1,7,6,2,3,5,6,7,9]
    rs = [0 for _ in range(len(nums))]
    print(rs)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = sorted(nums,reverse=True)
    print(b)
    # [9, 7, 7, 6, 6, 5, 3, 2, 1]
    n = 0 # n记录优先顺序
    for val in b:
        if val in nums:
            j = nums.index(val)
            rs[j] = n
            n += 1
            nums[j] = -1
    return rs
    # [8, 1, 3, 7, 6, 5, 4, 2, 0]

def numSorted_1(nums):
    a = [[nums[i], i] for i in range(len(nums))]
    print(a)
    # [[1, 0], [7, 1], [6, 2], [2, 3], [3, 4], [5, 5],
    # [6, 6], [7, 7], [9, 8]]

    a.sort(reverse=True)
    print(a)
    # [[9, 8], [7, 7], [7, 1], [6, 6], [6, 2], [5, 5],
    # [3, 4], [2, 3], [1, 0]]

    b = [a[i] + [i] for i in range(len(a))]
    print(b)
    # [[9, 8, 0], [7, 7, 1], [7, 1, 2], [6, 6, 3],
    # [6, 2, 4], [5, 5, 5], [3, 4, 6], [2, 3, 7], [1, 0, 8]]

    b = sorted(b, key=lambda x: x[1]) # 按照第二个位置升序
    print(b)
    # [[1, 0, 8], [7, 1, 2], [6, 2, 4], [2, 3, 7], [3, 4, 6],
    # [5, 5, 5], [6, 6, 3], [7, 7, 1], [9, 8, 0]]

    return [b[i][2] for i in range(len(b))]
    # [8, 2, 4, 7, 6, 5, 3, 1, 0]
    # 两个7，这种方法是不稳定的



if __name__ == '__main__':
    nums = [1,7,6,2,3,5,6,7,9]
    print(numSorted_2(nums))