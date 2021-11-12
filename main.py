# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def lcs(a, b):
    dp_table = [[0 for i in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp_table[i][j] += 1
                dp_table[i][j] += dp_table[i-1][j-1]
            else:
                dp_table[i][j] += my_max(dp_table, i, j)
    return dp_table[len(a)][len(b)]




def my_max(dp_table, i, j):
    a = dp_table[i-1][j]

    b = dp_table[i][j-1]
    return max_calcualtor(a, b)



def max_calcualtor(a, b):
    return a if a > b else b

keys = [1, 6, 2, 5, 3]


def main():
#in root 2d array we store indeces of the optimal roots
    root = [[]]
    construct(root, 0, len(root))


def construct(root, i, j):
    if i == 0 & j == len(root):
        print(keys[root[0][len(root)]] + 'is the root')
    else:
        print(keys[root[i][j-1]] + ' is left child of ' + keys[root[i][j]])
        print(keys[root[i-1][j]] + ' is right child of ' + keys[root[i][j]])
    construct(root, i, keys[root[i][j]])
    construct(root, keys[root[i][j]], j)

if __name__ == '__main__':
    main()

