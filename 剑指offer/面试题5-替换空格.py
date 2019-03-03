
# 第一次就做对了~过过过

def ReplacBlankMe(str1):
    str1 = str1.split()
    rs = str1[0]
    for i in range(1,len(str1)):
        rs += "%20"+str1[i]
    # print(type(rs))
    return rs

# 书中的方法

if __name__ == '__main__':
    str1 = "We are happy."
    print(ReplacBlankMe(str1))


