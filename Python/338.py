# 给一个非负数num，求从0到num每一个的数字的二进制中1的个数
# 结果返回一个数组对应每个数字的结果
# 大数的结果包含小数的结果，明显为递归问题
# 第一个数结果为0，从第二个数开始递归

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]*(num+1)
        for i in range(1, num+1):
            result[i] = result[i >> 1] + (i & 1)
        return result


s = Solution()
print(s.countBits(5))

# 0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111
# 写出来一串二进制数 看规律 100 和 1001 的前三位是一样的，增加一位1或0。
# 另一个事实是如果数是偶数最后一位二进制是0 奇数为1 所有递推式为res[i] = res[i>>1]+(i&1)
