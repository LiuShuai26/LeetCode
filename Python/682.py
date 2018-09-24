# 基础技巧题，使用栈
# ["5","2","C","D","+"]
# 数字为得分 C为上局分数无效 D为目前得分乘以二 +为上两轮的得分之和


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
