class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans=[]
        k=0
        for i in range(0,len(s)):
            # print(step)
            cur_list=[]
            if k>=len(s):
                break
            for j in range(i,len(s)):
                print(s[j:k+1])
            k+=1
        #         if cur_s==cur_s[::-1]:
        #             cur_list.append(cur_s)
        #             print(cur_s)
        #     ans.append(cur_list)
        #     print(cur_list)
        # print(ans)



if __name__ == '__main__':
    s = "aab"
    myResult = Solution()
    print(myResult.partition(s))