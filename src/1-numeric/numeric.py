# coding=utf-8
from __future__ import print_function
import math

#
#
# class Solver:
#     def calculate(self, a, b, c):
#         d = b ** 2 - 4 * a * c
#         if d >= 0:
#             disc = math.sqrt(d)
#         else:
#             print("error")
#         root1 = (-b + disc) / (2 * a)
#         root2 = (-b - disc) / (2 * a)
#         print(root1, root2)
#
#
# Solver().calculate(1, -2, 1)


print(3 / 2)  # 整数相除不会丢失小数部分
print(7 // 2)  # 整除

text = r"这是一个相当长的字符串包含\n\
几行文本, 就像你在 C 里做的一样."

print(text)  # r 表示原始字符串，不会舍弃\n

word = "abc" * 5
print(word[0:5])  # 分片处理，字符串不会从右边开始数

f0, f1 = 0, 1
while f1 < 10:
    print(f1, end=",")
    f0, f1 = f1, f0 + f1

