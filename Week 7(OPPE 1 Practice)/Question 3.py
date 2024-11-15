def minor_matrix(M, i, j):
    # Remove the ith row and jth column from matrix M
    return [row[:j] + row[j+1:] for idx, row in enumerate(M) if idx != i]

