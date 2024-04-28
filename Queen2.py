def place(k, i, x):
    for j in range(1, k):
        if x[j] == i or abs(x[j] - i) == abs(j - k):
            return False
    return True

def print_board(n, x, result_num):
    print("Result", result_num, ":")
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            if x[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print()

def NQueens(k, n, x, result_num):
    if k > n:
        print_board(n, x, result_num)
    else:
        for i in range(1, n + 1):
            if place(k, i, x):
                x[k] = i
                NQueens(k + 1, n, x, result_num)

n = 5
x = [0] * (n + 1)

# Start recursion to find all solutions
for result_num in range(1, n + 1):
    NQueens(1, n, x, result_num)
