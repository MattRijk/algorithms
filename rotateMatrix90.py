def rotate(matrix):
    if matrix is None or len(matrix)<1:
        raise Exception('must be nxn matrix')
    else:
        if len(matrix)==1:
            return matrix
        else:
            #solution matrix
            result = [row[:] for row in matrix]
            #size of matrix
            m = len(matrix[0])
                    
            for x in range(0,m):
                for j in range(0,m):
                    result[j][m-1-x] = matrix[x][j]
    return result

rotate(matrix)
# start
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# output
# [[7, 4, 1], 
#  [8, 5, 2], 
#  [9, 6, 3]]

