# 一个英文句子，要求分别反转每个单词


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 'bring it on'
        # 'no ti gnirb' 先将整个字符串反转
        # ['no', 'ti', 'gnirb'] 按空格分割
        # ['gnirb', 'ti', 'no'] 将每个词反转过来
        # gnirb ti no 按空格接成字符串
        return ' '.join(s[::-1].split(' ')[::-1])





# class Solution:
# #     def reverseWords(self, s):
# #         """
# #         :type s: str
# #         :rtype: str
# #         """
# #         result = ''
# #         s = s[::-1]
# #         for i in reversed(s.split(' ')):
# #             result = result + i + ' '
# #         return result[:-1]

s = Solution()
print(s.reverseWords('bring it on'))
