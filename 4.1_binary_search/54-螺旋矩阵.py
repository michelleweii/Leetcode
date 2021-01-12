class Solution:
    def spiralOrder(self, matrix):
        res = []
        row = len(matrix)
        col = len(matrix[0])
        x1,y1 = 0,0
        x2,y2 = row-1,col-1
        while x1 <= x2 and y1 <= y2:
            # print(x1,y1)
            for i in range(x1, x2+1):
                res.append(martix[y1][i])
                # print(martix[y1][i])

            for j in range(y1+1,y2+1):
                res.append(martix[j][x2])
                # print(martix[j][x2])
            # print(x2,y2)
            # print('-----')
            if x1<x2 and y1<y2:
                for i in range(x2-1,x1,-1):
                    res.append(martix[y2][i])
                    # print(martix[y2][i])
                # print('------')
                for j in range(y2,y1,-1):
                    res.append(martix[j][x1])
                    # print(martix[j][x1])

            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1

        return res

if __name__ == '__main__':
    martix = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
            ]
    print(Solution().spiralOrder(martix))

#         # result = list()
#         # if not matrix:
#         #     return result
#         # r, c = len(matrix), len(matrix[0])
#         # x1, y1, x2, y2 = 0, 0, c - 1, r - 1
#         # while x1 <= x2 and y1 <= y2:
#         #     print(x1,y1)
#         #     for i in range(x1, x2 + 1):
#         #         result.append(matrix[y1][i])
#         #
#         #     for j in range(y1 + 1, y2 + 1):
#         #         result.append(matrix[j][x2])
#         #     if x1 < x2 and y1 < y2:
#         #         for i in range(x2 - 1, x1, -1):
#         #             result.append(matrix[y2][i])
#         #
#         #         for j in range(y2, y1, -1):
#         #             result.append(matrix[j][x1])
#         #
#         #     x1 += 1
#         #     y1 += 1
#         #     x2 -= 1
#         #     y2 -= 1
#         #
#         # return result