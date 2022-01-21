def cavityMap(grid):
    for row, string in enumerate(grid):
        if row == 0 or row == (len(grid) - 1):
            continue
        else:
            for col, char in enumerate(string):
                if (
                    col == 0
                    or col == (len(string) - 1)
                    or grid[row][col - 1] == "X"
                    or grid[row - 1][col] == "X"
                    or grid[row + 1][col] == "X"
                    or grid[row][col + 1] == "X"
                ):
                    continue
                elif (
                    int(char) > int(grid[row][col - 1])
                    and int(char) > int(grid[row - 1][col])
                    and int(char > grid[row + 1][col])
                    and int(char) > int(grid[row][col + 1])
                ):
                    newstring = list(string)
                    newstring[col] = "X"
                    grid[row] = "".join(newstring)

    return grid
