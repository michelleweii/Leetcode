"""
middle
双指针同向，滑动窗口
利用滑动窗口法，左右指针起点都为原数组的首位。
实现步骤如下：
1、不断右移右指针，使窗口不断增大；
2、当窗口内出现一个不同的元素时，就可以将元素及其数量（等于左右指针之差）更新在数组中，然后让左指针指向右指针；
3、遍历到最后一个字符时也需要结算，因此将右指针的终点设为数组之外一格。当右指针移到终点时也要更新数组。
"""
class Solution(object):
    def compress(self, chars):
        left, right = 0, 0
        size = 0
        n = len(chars)
        while right <= n:
            # 遍历完成，或右指针元素不等于左指针元素时，更新数组
            if right==n or chars[right]!=chars[left]:
                # 更新数组
                chars[size] = chars[left]
                size += 1
                # 更新计数，当个数大于 1 时才更新
                if (right - left > 1):
                    i2str = str(right-left)
                    for x in i2str:
                        chars[size] = x
                        size += 1

                left = right
            right += 1

        print(chars) # ['a', '2', 'b', '2', 'c', '3', 'c']
        return size # 6

if __name__ == '__main__':
    # chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    chars = ["a","a","b","b","c","c","c"]
    myResult = Solution()
    print(myResult.compress(chars))