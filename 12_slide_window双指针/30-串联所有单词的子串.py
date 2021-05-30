"""
hard
哈希表+双指针
o(n*mw)
枚举所有子串的开头，从这个单词开始，查看所有的[i,i+w,i+2w,...,i+(m-1)w)，
判断单词是否已经用过了，这个单词是否和hashmap中的一致
o(n*w)
[i,i+w,i+2w,...,i+(m-1)w),[i+(m-1)w), [i+(m-1)w, i+mw)
i=0, w, 2w, 3w,...
i=1, w+1, ...
...
i=w-1
"""
class Solution:
    def findSubstring(self, s, words):
        res = []
        n = len(s)
        m = len(words) # 给定单词的长度, 时间复杂度于此无关
        w = len(words[0])
        hash_map = {}

        # 统计每种单词出现的个数，因为会有重复单词
        for i in range(m):
            hash_map[words[i]] = hash_map.get(words[i],0)+1
        # print(hash_map) # {'foo': 1, 'bar': 1}


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(Solution().findSubstring(s, words))
    # [0,9]

    # s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]
    # []