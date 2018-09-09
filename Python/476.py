class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while num >= i:  # i是当前长度的二进制数字的最小值，如果num < i，则i的长度大于num
            num ^= i    # i为1、10、100、1000，此操作是把num的每一位依次翻转
            i <<= 1
        return num