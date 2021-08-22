# 7_dynamic_programming
class Solution(object):
    def countSubstrings(self, s):
        new_word = []
        for i in range(len(s)):
            for k in range(1,len(s)):
                # print(k)
                if i+k > len(s):
                    end = len(s)
                    print(end)
                    new_word.append(s[i:end])
                    break
                else:
                    new_word.append(s[i:i+k])

        print(new_word)

        count = 0
        while len(new_word):
            length = len(new_word)
            tmpword = new_word[::-1]  # 反转字符串
            if (length == 1):
                count += 1
                continue
            else:
                for i, val_i in enumerate(new_word):
                    if (i > (length / 2 - 1)):
                        count+=1
                        continue
                    if (val_i != tmpword[i]):
                        continue
                    count+=1
            new_word = new_word[:-1]

        print(count)


if __name__ == '__main__':
    s = "abc"
    myResult = Solution()
    print(myResult.countSubstrings(s))