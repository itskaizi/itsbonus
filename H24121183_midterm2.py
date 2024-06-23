import random

def generate_path(N, M):
    maze = [[' ' for _ in range(M)] for _ in range(N)]
    x, y = 0, 0

    while (x, y) != (N - 1, M - 1):
        if y == M - 1:
            x += 1
        elif x == N - 1:
            y += 1
        else:
            if random.choice([True, False]):
                y += 1
            else:
                x += 1
        maze[x][y] = ' '
    
    return maze

def add_obstacles(maze, num_obstacles):
    N, M = len(maze), len(maze[0])
    indexes = [i for i in range(N * M)]
    obstacles_indexes = random.sample(indexes, num_obstacles)
    for index in obstacles_indexes:
        row = index // M
        col = index % M
        maze[row][col] = 'X'

    return maze

def print_maze(maze):
    print("+" + "---+" * len(maze[0]))
    for i in range(len(maze)):
        row_str = "|"
        for j in range(len(maze[0])):
            if maze[i][j] == ' ':
                row_str += "   "
            else:
                row_str += " X "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

# prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = (N - 1) * (M - 1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

# generate the maze using the user-specified values
maze = generate_path(N, M)
add_obstacles(maze, num_obstacles)

# print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)