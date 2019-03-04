# del[1:3]删除指定区间
class Solution(object):
    def compress(self, chars):
        # 双指针
        

    def compress1(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        char_map = {}
        for index,val in enumerate(chars):
            if val not in char_map:
                char_map[val] = 1
            else:
                cnt = char_map[val]
                cnt += 1
                char_map[val] = cnt
        rs = []
        for key in char_map:
            rs.append(key)
            if char_map[key] == 1:
                continue
            else:
                rs.append(str(char_map[key]))
        print(rs)
        length = "".join(rs)
        return len(length)


def main():
    chars = ["a","a","b","b","c","c","c"]
    myResult = Solution()
    print(myResult.compress(chars))

if __name__ == '__main__':
    main()