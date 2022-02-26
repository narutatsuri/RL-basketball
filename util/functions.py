

def column(matrix, i):
    """
    Gets column of matrix. 
    INPUTS:     Array, Int of column to look at
    RETURNS:    Array of the column
    """
    return [row[i] for row in matrix]