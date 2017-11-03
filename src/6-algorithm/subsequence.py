import numpy as np

word_a = 'fort'
word_b = 'fish'
word_c = 'fosh'


def subseq(word1, word2):
    row = len(word1)
    column = len(word2)
    cell = np.array(np.zeros(row*column).reshape(row, column), dtype=int)
    for i in range(row):
        for j in range(column):
            up = 0 if (i - 1 < 0) else cell[i - 1][j]
            left = 0 if (j - 1 < 0) else cell[i][j - 1]
            if word1[i] == word2[j]:
                if i - 1 >= 0 and j - 1 >= 0:
                    cell[i][j] = cell[i - 1][j - 1] + 1
                else:
                    cell[i][j] = 1
            else:
                cell[i][j] = max(left, up)
    print cell


subseq(word_a, word_c)
subseq(word_b, word_c)
