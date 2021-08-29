"""
hard bfs最短路径
20210825 一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！
# https://www.acwing.com/solution/content/221/
思路：
1、将单词看做点，如果两个单词可以相互转化，则在相应的点之间连一条无向边。那问题就变成了求从起点到终点的最短路。
2、枚举每个单词，然后枚举该单词的每一位字母，再枚举这一位的所有备选字母，然后再判断改变后的字符串是否存在，时间复杂度 O(26nL2)。
# A* 只有 终点第一次出队时才保证距离最短，其余点第一次出队不保证最小的原则
"""
# hit-hot-dot-dog-cog
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if len(wordList)==0 or endWord not in wordList:return 0
        q = [] # 定义队列
        dist = {} # 记录距离
        word_set = set(wordList) # 合法状态

        dist[beginWord] = 1
        q.append(beginWord)

        while q:
            tmp = q.pop(0)
            r = tmp
            # 枚举该tmp单词的每一位字母
            for i in range(len(tmp)):
                # 再枚举i这一位的所有备选字母
                for j in range(26):






if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # 5
    print(Solution().ladderLength(beginWord,endWord,wordList))