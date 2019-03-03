# 一个256*256的二维数组，逆时针旋转90度

def Rotate(nums):
    row = len(nums)
    # print(row)
    column = len(nums[0])
    # print(column)
    B = [[0 for _ in range(row)] for _ in range(column)]
    print(B)
    for i in range(row):
        for j in range(column-1,-1,-1):
            # print(j)
            B[i][j] = nums[j][row-1-i]

    return B


if __name__ == '__main__':
    nums = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    print(nums)
    print("Rotating...")
    print(Rotate(nums))