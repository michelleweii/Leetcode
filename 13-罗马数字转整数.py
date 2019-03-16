class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        hash_map = {}
        hash_map['I'] = 1
        hash_map['V'] = 5
        hash_map['X'] = 10
        hash_map['L'] = 50
        hash_map['C'] = 100
        hash_map['D'] = 500
        hash_map['M'] = 1000
        for i in range(len(s)-1):
            if (hash_map[s[i]]<hash_map[s[i+1]]):
                res -= hash_map[s[i]]
            else:
                res += hash_map[s[i]]
        return res+hash_map[s[-1]]


if __name__ == '__main__':
    s = "IV"
    print(Solution().romanToInt(s))