import sys
def fn1(s):
    s = s.split(' ')
    s = [i for i in s if i!='']
    # print(s)
    s.reverse()
    # print(s)
    return " ".join(s)



if __name__ == '__main__':
    # s = 'the sky is            blue!'
    s = sys.stdin.readline().strip()
    res = fn1(s)
    print(res)