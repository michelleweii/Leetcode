"""
给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。
如果继承词有许多可以形成它的词根，则用最短的词根替换它。
"""
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # root_dict = set(dict)
        # raws = sentence.split()
        # res = []
        # for raw in raws:
        #     flag = False
        #     for i in range(0, len(raw)):
        #         prefix = raw[0:i + 1]
        #         if prefix in root_dict:
        #             res.append(prefix)
        #             flag = True
        #             break
        #     if flag == False:
        #         res.append(raw)
        # return ' '.join(res)

        myDict = set(dict)
        res = []  # res由字符串变为列表就不内存溢出了
        for word in sentence.split(): # 字符串按空格划分
            cur_word = ""
            for i,ch in enumerate(word):
                cur_word += ch
                if cur_word in myDict:
                    res.append(cur_word)
                    break
                if i==len(word)-1:
                    res.append(word)
        return " ".join(res)




def main():
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    myresult = Solution()
    print(myresult.replaceWords(dict, sentence))


if __name__ == "__main__":
    main()
