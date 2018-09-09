
# When going left to right, we'll remember the index prev of the\
#  last character C we've seen. Then the answer is i - prev.
#
# When going right to left, we'll remember the index prev of the\
#  last character C we've seen. Then the answer is prev - i.
#
# We take the minimum of these two answers to create our final answer.

class Solution:
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):   #列举，返回值和值的下标
            if x == C:
                prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):     # 值从len(S)-1到0
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

#
















class Solution0:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        left = False    # 表示左边有C
        right = False
        count = 0
        start = 0       # 从这里开始计算结果
        result = [0] * len(S)
        for i in range(0, len(S)):
            if S[i] == C and not right:     # 如果第一次遇到C则，把状态设为右边有C
                right = True
            elif S[i] == C and right:       # 如果遇到C，右边值为真，则状态为两边都有C
                left = True
            elif S[i] != C and i == len(S)-1:   # 如果都最后一个字符还没遇到C，则状态为左边有C
                right = False
                left = True

            if S[i] != C:
                count += 1

            if S[i] == C and not left and right:    # 计算结果，状态为右边有C
                for j in range(start, i):
                    result[j] = count
                    count -= 1
                start = i+1
                count = 0
            if S[i] == C and left and right:    # 计算结果，状态为两边都有C
                if count % 2 == 0:
                    mid = int(count/2)
                    num = 1
                    for j in range(start, i):
                        if num <= count/2:
                            result[j] = num
                            num += 1
                        else:
                            result[j] = mid
                            mid -= 1
                else:
                    mid = int(count/2)
                    num = 1
                    for j in range(start, i):
                        if num <= count/2 + 1:
                            result[j] = num
                            num += 1
                        else:
                            result[j] = mid
                            mid -= 1
                count = 0
                start = i+1
            if i == len(S)-1 and left and not right:    # 左边有C，右边无
                num = 1
                for j in range(start, len(S)):
                    result[j] = num
                    num += 1
        return result


S = "loveleetcode"
C = 'e'

s = Solution()
print(s.shortestToChar(S, C))
