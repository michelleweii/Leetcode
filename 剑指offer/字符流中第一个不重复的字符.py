# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    """
    def __init__(self):
        self.Q = []
        self.hashmap = {}

    def FirstAppearingOnce(self):
        if self.Q:
            return self.Q[0]
        return "#"

    def Insert(self, char):

        if char in self.hashmap:
            self.hashmap[char] += 1
            if not self.Q:
                self.Q.pop()
        else:
            self.hashmap[char] = 1
            self.Q.append(char)
        # 因为list是可变的，所以每次会改变都是null
        # 要用str不可变，深拷贝的方法待完成
        """
    def __init__(self):
        self.Q = ""
        self.hashmap = {}

    def FirstAppearingOnce(self):
        if self.Q:
            return self.Q[0]
        else: return "#"

    def Insert(self, char):

        if char in self.hashmap:
            self.hashmap[char] += 1
            while len(self.Q)>0 and self.hashmap[self.Q[0]]>1:
                self.Q = self.Q[:-1]
        else:
            self.hashmap[char] = 1
            self.Q = self.Q+char
        print(self.Q)



if __name__ == '__main__':
    s = "BabyBaby"
    # print(s[:-1])
    for ch in s:
        Solution().Insert(ch)
    print(Solution().FirstAppearingOnce())