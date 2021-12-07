"""
hard 2021-12-07 bfs
找出并返回所有从 beginWord 到 endWord 的 最短转换序列, 注意是“所有”&“最短路径”->BFS
基础题127（求最短转化序列的长度）
"""
#
class Solution:
    def __init__(self):
        self.res = []

    def findLadders(self, beginWord: str, endWord: str, wordList): #: List[str]) -> List[List[str]]:
        if len(wordList) == 0 or endWord not in wordList: return []
        wordset = set(wordList)
        if beginWord in wordset: wordset.remove(beginWord)

        # 图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        queue = []
        queue.append(beginWord)
        visited = set(beginWord)
        word_len = len(beginWord) # 每个单词的长度，用于遍历char，进行char替换

        finish = False
        step = 1
        while queue:
            cur_level_size = len(queue)
            cur_path = []
            # 1、遍历当前层待替换单词
            for i in range(cur_level_size):
                # 依次遍历当前队列中的单词
                word = queue.pop(0)
                wordlist = list(word)
                cur_path.append(word)
                # 2、遍历单词的每一个字符
                for j in range(word_len):
                    ori_char = word[j]
                    # 3、遍历26位字母
                    for k in range(26):
                        wordlist[j] = chr(ord('a') + k)
                        new_word = ''.join(wordlist)
                        if new_word in wordset:

                            if new_word==endWord:
                                finish = True
                            else: cur_path.append(new_word)

                            if new_word not in visited:
                                queue.append(new_word)
                                visited.add(new_word)

                    # 恢复原始单词
                    wordlist[j] = ori_char
            print(cur_path)

        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    print(Solution().findLadders(beginWord, endWord, wordList))