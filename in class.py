# 1)
# str = "1 4 3 5 7 10021312 3821 -12391"

# a = str.split()

# l = len(a)
# for i in range(0, 1):
#     if int(a[i]) > 3:
#         print(a[i])
# print('\n')

# 2)
# l = []
# l2 = [1, 10]
# l.append(l2)
# l2 = [10, 100]
# l.append(l2)
# l2 = [20, 200]
# l.append(l2)

# rows = 3;
# cols = 2;
# for i in range (0, rows, 1):
#     for j in range (0, cols, 1):
#         print(l[i][j])
#         print(" ")
#     print('\n')

#3)
# f = open("inputdata")

# data = []
# l = 200l = f.readline()
# while l != ""

# In Class Ex 1
# X = [[12, 7],
#     [4, 5],
#     [3, 8]]

# result = [[0,0,0],
#          [0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[j][i] = X[i][j]
        
# for r in result:
#     print(r)

# In Class ex 2: Add two matrices

# X = [[12, 7, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
    
# Y = [[5, 8, 1],
#     [6, 7, 3],
#     [4, 5, 9]]
    
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]
        
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j] = X[i][j] + Y[i][j]
        
# for r in result:
#     print(r)

# In Class exercise 3: Write a python program to multiply two matrices
matrix_a = [[1, 2], 
            [3, 4]]
matrix_b = [[5, 6], 
            [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = (matrix_a[i][0] * matrix_b[0][j] +
                        matrix_a[i][1] * matrix_b[1][j])

for row in result:
    print(row)


        


