#   Simple maze - Codewars
#   Nilton Gomes Martins Junior
#   11/04/2020
#   https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c/python

def has_exit(maze):
    #   Assumes that maze is always rectangular (possibly square?) with at least one position.
    #   TODO:   Problem description states the maze may not always be rectangular. In these cases, we could generalize fill the maze until it becomes a rectangle, considering the length of the longest row and adding '#' blocks to either side of the smaller rows.
    num_rows = len(maze)
    num_cols = len(maze[0])

    #   Finds the coordinates of 'k'.
    kate_found = False
    for row_index in range(num_rows):
        col_index = maze[row_index].find('k')  
        if col_index != -1:
            #  There should be no multiple 'k's.
            if kate_found:
                raise Exception("There should be no multiple Kates")
            row_k = row_index
            col_k = col_index
            kate_found = True
        
    #   Checks if 'k' is at the border.
    if row_k == 0 or row_k == num_rows - 1 or col_k == 0 or col_k == num_cols - 1:
        return True

    #   List of next mazes to check by moving 'k' to the nearest open positions. The 'k' is definetly not on the border of the maze.
    new_mazes = []
    #   Up.
    if maze[row_k - 1][col_k] == ' ':
        temp_maze = [row for row in maze]
        temp_maze[row_k - 1] = temp_maze[row_k - 1][:col_k - 1] + 'k' + temp_maze[row_k - 1][col_k + 1:]
        temp_maze[row_k] = temp_maze[row_k][:col_k - 1] + '#' + temp_maze[row_k][col_k + 1:]
        new_mazes.append(temp_maze)
    #   Down.
    if maze[row_k + 1][col_k] == ' ':
        temp_maze = [row for row in maze]
        temp_maze[row_k + 1] = temp_maze[row_k + 1][:col_k - 1] + 'k' + temp_maze[row_k + 1][col_k + 1:]
        temp_maze[row_k] = temp_maze[row_k][:col_k - 1] + '#' + temp_maze[row_k][col_k + 1:]
        new_mazes.append(temp_maze)
    #   Right.
    if maze[row_k][col_k + 1] == ' ':
        temp_maze = [row for row in maze]
        temp_maze[row_k] = temp_maze[row_k].replace(" k", "k#")
        new_mazes.append(temp_maze)
    #   Left.
    if maze[row_k][col_k - 1] == ' ':
        temp_maze = [row for row in maze]
        temp_maze[row_k] = temp_maze[row_k].replace("k ", "#k")
        new_mazes.append(temp_maze)
    
    for new_maze in new_mazes:
        if has_exit(new_maze):
            return True
    
    return False

if __name__ == "__main__":
    maze = ["########",
        "# # ## #",
        "# #k#  #",
        "# # # ##",
        "# # #  #",
        "#     ##",
        "########"]
    print(has_exit(maze))    



