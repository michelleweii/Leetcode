# 68. 文本左右对齐 hard
# 考察点：

class Solution:
    def fullJustify(self, words, maxWidth):
        if not words:
            return ['']
        result = []
        i = 0
        tmpLen = 0  # 记录当前行单词+' '的长度
        counts = 0  # 记录当前行的单词个数
        while i < len(words):
            if tmpLen + len(words[i]) <= maxWidth:
                tmpLen += len(words[i]) + 1
                i += 1
                counts += 1
            else:
                numSpace = maxWidth - tmpLen + counts  # 空格总数
                # print(i,numSpace,(tmpLen,counts))
                if counts == 1:
                    result.append(words[i-1]+' '*numSpace)
                else:
                    eachNum = numSpace // (counts-1)  # 单词之间应放的空格数
                    restNum = numSpace % (counts-1)  # 剩余空格数
                    tmp = ''
                    start = i - counts
                    while start < i - 1:
                        if restNum > 0:
                            # print(' ' * (eachNum + 1),eachNum + 1)
                            tmp = tmp + words[start] + ' ' * (eachNum + 1)
                            restNum -= 1
                            start += 1
                        else:
                            tmp = tmp + words[start] + ' ' * eachNum
                            start += 1
                    tmp = tmp + words[i-1]
                    result.append(tmp)
                tmpLen = 0
                counts = 0
        # 最后一行
        if counts != 0:
            j = counts
            tmp = ''
            while j > 1:
                tmp = tmp + words[i-j] + ' '
                j -= 1
            tmp = tmp + words[i-1]
            tmp = tmp + ' ' * (maxWidth-len(tmp))
            result.append(tmp)
        return result

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words,maxWidth))