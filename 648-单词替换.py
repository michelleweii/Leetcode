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
        myDict = {}
        res = ""
        for word in dict:
            if word in myDict:
                myDict[word]+=1
            else:
                myDict[word]=1
        # print(myDict)

        for word in sentence.split(): # 字符串按空格划分
            cur_word = ""
            for i,ch in enumerate(word):
                cur_word += ch
                if cur_word in myDict:
                    if res == "":
                        res += cur_word
                    else:res += ' '+cur_word
                    break
                if i==len(word)-1:
                    if res == "":
                        res+=word
                    else:
                        res += ' '+word
        return res




def main():
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    myresult = Solution()
    print(myresult.replaceWords(dict, sentence))


if __name__ == "__main__":
    main()
