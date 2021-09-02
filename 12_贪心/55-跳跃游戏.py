class Solution(object):
    def canJump(self, nums):
        # 最远可达到的位置（index），不是落脚点，落脚点是这段中最远的位置
        far = [] # 最远可以跳至的位置
        for i, val in enumerate(nums):
            temp = i+val
            far.append(temp)
        # print(far)
        max_far = far[0]
        jump = 0
        # jump(当前位置)要<=最远能到的位置，这样才有路可以走
        # 如果我现在处于的位置<最远能调到的位置，那么就一定true
        while jump<len(nums) and jump<=max_far:
            # 直到jump跳至数组尾部orjump超越了当前可以跳的最远位置
            if far[jump]>max_far:
                # 如果当前可以跳的更远，则更新max_far
                max_far = far[jump]
            jump += 1


        if jump == len(nums):
            return True
        return False


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))