class Solution(object):
    def lengthOfLongestSubstring(self, s):

        hash_map = {}
        left,res = 0,0
        for i in range(len(s)): # i就是now，
            # 如果当前字符从没出现过，或者是出现了，但不包含在当前窗口内：
            if s[i] not in hash_map or left>hash_map[s[i]]:
               res = max(res,i-left+1)
            else:
                left = hash_map[s[i]]+1

            hash_map[s[i]] = i
        print(hash_map)
        return res



    def lengthOfLongestSubstringPiggy(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s)==1:
        #     return 1
        hash_map = {}
        max_len = 0
        i,j = 0,0
        for index,val in enumerate(s):
            if index==0:
                hash_map[val] = index
            if val not in hash_map or hash_map[val] > i:
                hash_map[val] = index
                j += 1
            else:

                i,j = hash_map[val]+1,hash_map[val]+1
                hash_map[val] = index
                # print(i)

            cur_len = j - i + 1
            if cur_len > max_len:
                max_len = cur_len


        return max_len




if __name__ == '__main__':
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))