# We ask what feature makes two coordinates (r1, c1) and (r2, c2)\
#  belong to the same diagonal?
#
# It turns out two coordinates are on the same diagonal \
# if and only if r1 - c1 == r2 - c2.
#
# This leads to the following idea: \
# remember the value of that diagonal as groups[r-c].\
#  If we see a mismatch, the matrix is not Toeplitz; otherwise it is.



class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        group = {}
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if i-j not in group:
                    group[i-j] = x
                else:
                    if group[i-j] != x:
                        return False
        return True

