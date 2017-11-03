# coding=utf-8
word_a = 'fish'
word_b = 'hish'

row = len(word_a) + 1
column = len(word_b) + 1
cell = [[0 for j in range(column)] for i in range(row)]

for i in range(1, row):
    a = word_a[i - 1]
    for j in range(1, column):
        b = word_b[j - 1]
        if word_a[i - 1] == word_b[j - 1]:
            cell[i][j] = cell[i - 1][j - 1] + 1
print cell
result = [[cell[i][j] for j in range(1, column)] for i in range(1, row)]
print result

# 最终答案取cell中的最大值
