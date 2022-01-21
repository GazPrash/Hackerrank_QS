def surfaceArea(A):
    n = len(A)
    area = (6 * (len(A[0]))) * n
    extra_sum = 0
    for lists in A:
        print(extra_sum)
        extra_sum += 4 * ((sum(lists)) - 1 * len(lists))

    area += extra_sum

    for index_row, rows in enumerate(A):
        for index_col, cols in enumerate(rows):
            if (index_row > 0):
                if (index_row > 0) and cols - A[index_row - 1][index_col] <= 0:
                    area -= cols
                elif cols - A[index_row - 1][index_col] > 0:
                    area -= A[index_row - 1][index_col]

            if (index_row < (n-1)):
                if cols - A[index_row + 1][index_col] <= 0:
                    area -= cols
                elif cols - A[index_row + 1][index_col] > 0:
                    area -= A[index_row + 1][index_col]

            if (index_col > 0):
                if cols - A[index_row][index_col - 1] <= 0:
                    area -= cols
                elif cols - A[index_row][index_col - 1] > 0:
                    area -= A[index_row][index_col - 1]

            if index_col < (len(A[0])-1):
                if cols - A[index_row][index_col + 1] <= 0:
                    area -= cols
                elif cols - A[index_row][index_col + 1] > 0:
                    area -= A[index_row][index_col + 1]

    print(area)

#              | 3 |  3 |   
#      | 2 |   |   |    |      
#      |   | 1 |   |    | 1 |

surfaceArea([[1]])
