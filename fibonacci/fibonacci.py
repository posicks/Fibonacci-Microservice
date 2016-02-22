'''
Created on Feb 20, 2016

@author: Steve Posick
'''

'''
[1 1] = [F(n+1),   F(n)]
[1 0]   [  F(n), F(n-1)]
'''
FIBONACCI_START_MATRIX = [[1, 1], [1, 0]]


def matrix_muliply(A, B):    
    result = [[0, 0], [0, 0]]
    
    m1Rows = len(A[0])
    m1Columns = len(B[0])
                    
    for ARow in range(m1Rows):
        # iterate through columns of matrix A
        for BColumn in range(m1Columns):
            # iterate through rows of matrix B
            for index in range(m1Columns):
                result[ARow][BColumn] += (A[ARow][index] * B[index][BColumn])

    return result


def matrix_power(A, n):
    if n <= 1:
        return A
    
    result = [[1, 0], [0, 1]]
    
    '''
    Exponentiation by squaring
    '''
    while n != 0:
        if (n & 0x01) != 0:
            result = matrix_muliply(result, A)
        
        n = n >> 1
        A = matrix_muliply(A, A)
    
    return result


def fibonacci_matrix(start, length):
    if start < 0:
        raise ValueError('start must be greater than or equal to 0 (start >= 0)')
    elif length < 1:
        raise ValueError('length must be greater than 0 (length > 0)')
        
    
    result = [0 for i in range(length)]
    matrix = matrix_power(FIBONACCI_START_MATRIX, start)
    
    if start == 0:
        result[0] = matrix[1][1]
        if length > 1:
            result[1] = matrix[0][1]
    else:
        result[0] = matrix[0][1]
        if length > 1:
            result[1] = matrix[0][0]

    for i in range(2, length):
        result[i] = result[i-1] + result[i-2]

    return result
