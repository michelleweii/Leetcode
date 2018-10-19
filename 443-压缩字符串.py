# del[1:3]删除指定区间
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans = ''
        length = len(chars)
        i = 0
        while i<length:
            count = 1
            while i<(length-1) and chars[i+1]==chars[i]:
                count+=1
                i+=1
            print(count) #2 2 3
            ans += chars[i]
            print(ans)
            if count>1:
                ans += str(count)
            i+=1

        # print(ans)
        ans = list(ans)
        print(chars)
        for j in range(len(ans)):
            chars[j] = ans[j]
        print(chars)
        return len(ans)

def main():
    chars = ["a","a","b","b","c","c","c"]
    myResult = Solution()
    print(myResult.compress(chars))

if __name__ == '__main__':
    main()