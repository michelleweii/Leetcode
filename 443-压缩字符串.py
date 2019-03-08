# del[1:3]删除指定区间
class Solution(object):
    def compress22(self, chars):
        # 双指针
        pass

    def compress(self, chars):
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left


    def compress_no_in_place(self, chars):
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