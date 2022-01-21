def destructor(grid):
    note_down = []

    for rown, rows in enumerate(grid):
        for coln, col in enumerate(rows):
            if col == "O":
                note_down.append((rown, coln))

    return note_down


def bomberMan(n, grid):

    if n == 1:
        return grid


    ini = [["O" for x in range(len(grid[0]))] for x in range(len(grid))]
    if n%2 == 0:
        return ini

    note_down = destructor(ini)

    for i in range(n//2):
        print("times")
        new_grid = [["O" for x in range(len(grid[0]))] for x in range(len(grid))]
        for x, y in note_down:
            if grid[x][y] == "O":
                new_grid[x][y] = "."
                if x > 0:
                    new_grid[x-1][y] = "."
                if x < (len(new_grid) - 1):
                    new_grid[x+1][y] = "."
                if y > 0:
                    new_grid[x][y-1] = "."
                if y < (len(new_grid[0])-1):
                    new_grid[x][y+1] = "."

        grid = new_grid
        note_down = destructor(grid)


    grid = []

    for rows in new_grid:
        grid.append("".join(rows))

    print(grid)



bomberMan(5, ['.......', '...O.O.', '....O..','..O....', 'OO...OO', 'OO.O...'])
