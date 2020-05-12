#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start

## 1、首先考虑乘积的总位数，两个数相乘的最大位数为两数的位数之和，
##    所以先申请一个结果字符串位数为4，并且每一位都初始化为‘0’。
## 2、从第一个数的个位数‘8’开始，依次与“99”相乘。在乘法过程中
# 首先初始化每一位置的进位add为0，然后计算出对应单个位的乘积mul，
# 比如第一位8x9=72，然后取其个位与当前位置的数字以及前一位置的进位add相加得到sum，
# 此时sum为2+0+0=2，所以结果字符串的个位数字就为‘2’。
# 当前位置的进位add更新为mul的十位数与sum十位数之和，此时进位add为7+0=7。
## 3、算完一次单个位置的乘法后，最后将当前乘积的前一位更新为add，具体来说8x99=792，
# 但遍历完99后结果只记录了最后两位“92”，此时进位add为7，所以要将前一位更新为7。
## 4、计算完结果后要判断输出的总位数，因为可能出现结果字符串前几位都是0的情况，
# 找到第一位不是0的数字然后返回之后的字符串。

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''
        l1 = len(num1)
        l2 = len(num2)
        ans = [0] * (l1 + l2)
        for i in range(l1 - 1, -1, -1):
            carry = 0
            for j in range(l2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum = ans[i + j + 1] + mul % 10 + carry
                ans[i + j + 1] = sum % 10
                carry = mul // 10 + sum // 10
            ans[i] += carry
        index = 0
        while index < l1 + l2 and ans[index] == 0:
            index += 1
        if index == l1 + l2 :
            return '0'
        ans = ans[index:]
        return ''.join([str(i) for i in ans])

num1 = '0'
num2 = '0'
print(Solution().multiply(num1, num2))
        
# @lc code=end

