class MinStack:
    """
        2021/01/12 单调队列
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        pass

    def push(self, x):
        pass

    def pop(self):
        pass


    def top(self):
        pass

    def getMin(self):
        pass

if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    tmp = [-3,0,0,-2]
    for x in tmp:
        obj.push(x)
        obj.pop()
        param_3 = obj.top()
        param_4 = obj.getMin()
