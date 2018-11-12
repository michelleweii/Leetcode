class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        pos = []
        ans = []
        for i in range(len(seats)):
            if seats[i] == 1:
                pos.append(i)
        # print(pos)
        j = 0
        for i in range(len(seats)):
            if j<len(pos)-1:
                if seats[i] == 0:
                    ans.append(max(i-pos[j],pos[j+1]-i))
                    print(ans)
                    j+=1
        return max(ans)



def main():
    # seats = [1,0,0,0,1,0,1]
    seats = [1,0,0,0]
    myResult = Solution()
    print(myResult.maxDistToClosest(seats))

if __name__ == '__main__':
    main()