# 二项式相乘


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, a[:-1].split('+')) # map把第一个参数的函数作用在第二个参数的每个元素上
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1*b1 - a2*b2, a1*b2 + a2*b1)
