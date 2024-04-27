def place(k, i, x):
    for j in range(1, k):    #1 TO K-1 cause checking previous k-1 queens where they got placed
        if x[j] == i or abs(x[j] - i) == abs(j - k):  #x[j] is the part of array!
            return False
    return True

def NQueens(k, n, x):
    if k > n:                     #2
        print(x[1:])  # printing the placement of queens
    else:
        for i in range(1, n+1):
            if place(k, i, x):
                x[k] = i
                NQueens(k+1, n, x)

n = 4  # for example, setting the board size to 8x8
x = [0] * (n+1)  # array to store column positions of queens
NQueens(1, n, x)  # start with the first column



# x[j] represents the column number where a queen is already placed in the row indexed by j.
# i represents the column number where we are considering placing a queen in the current row k.
# So, x[j] == i checks if the column number of the existing queen in row j is the same as the column number where we want to place the queen in row k.

# If x[j] == i is True, it means there is already a queen in the same column as the one we are considering for placement in the current row, which would result in a conflict.




#2
# k represents the current row number.
# n represents the total number of rows/columns on the board.
# x is the list that stores the column positions of the queens.
# If k is greater than n, it means we have reached a row number greater than the total number of rows on the board. This indicates that all queens have been successfully placed on the board.