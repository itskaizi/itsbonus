import random

def generate_path(maze, N, M):
    r, c = 0, 0
    maze[(r, c)] = 2
    while r < N - 1 or c < M - 1:
        if r < N - 1 and c < M - 1:
            if random.choice([True, False]):
                r += 1
            else:
                c += 1
        elif r < N - 1:
            r += 1
        else:
            c += 1
        maze[(r, c)] = 2

def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0
    empty_cells = [(r, c) for r in range(N) for c in range(M) if maze[(r, c)] == 0]
    if min_obstacles > len(empty_cells):
        print(f"Too many obstacles. Max possible is {len(empty_cells)}.")
        return False
    while obstacles_added < min_obstacles:
        r, c = random.choice(empty_cells)
        if maze[(r, c)] == 0:
            maze[(r, c)] = 1
            obstacles_added += 1
            empty_cells.remove((r, c))
    return True

def set_obstacle(maze, N, M):
    try:
        r = int(input(f"Enter row (0 to {N-1}): "))
        c = int(input(f"Enter column (0 to {M-1}): "))
        if (r, c) not in maze or r < 0 or r >= N or c < 0 or c >= M:
            raise KeyError
        if maze[(r, c)] == 2:
            print("Cannot modify the path cell.")
        else:
            maze[(r, c)] = 1
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except KeyError:
        print("Coordinates are out of bounds.")

def remove_obstacle(maze, N, M):
    try:
        r = int(input(f"Enter row (0 to {N-1}): "))
        c = int(input(f"Enter column (0 to {M-1}): "))
        if (r, c) not in maze or r < 0 or r >= N or c < 0 or c >= M:
            raise KeyError
        if maze[(r, c)] == 2:
            print("Cannot modify the path cell.")
        elif maze[(r, c)] == 0:
            print("No obstacle at given coordinates.")
        else:
            maze[(r, c)] = 0
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except KeyError:
        print("Coordinates are out of bounds.")

def print_maze(maze, N, M):
    for r in range(N):
        for c in range(M):
            if maze.get((r, c)) == 0:
                print('   ', end='')
            elif maze.get((r, c)) == 1:
                print(' X ', end='')
            elif maze.get((r, c)) == 2:
                print(' O ', end='')
        print()

def main():
    while True:
        try:
            filename = input("Enter the maze file name: ")
            with open(filename, 'r') as file:
                lines = file.readlines()
                N = len(lines)
                M = len(lines[0].strip())
                maze = {(r, c): 0 for r in range(N) for c in range(M)}
                for r, line in enumerate(lines):
                    for c, char in enumerate(line.strip()):
                        if char == 'X':
                            maze[(r, c)] = 1
                break
        except IOError:
            print("File not found. Please enter a valid file name.")
    
    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles: "))
            if min_obstacles < 0:
                print("Number of obstacles must be non-negative.")
            else:
                if add_obstacles(maze, min_obstacles, N, M):
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    generate_path(maze, N, M)
    print_maze(maze, N, M)
    
    while True:
        print("Options: \n1. Set an obstacle\n2. Remove an obstacle\n3. Exit")
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                set_obstacle(maze, N, M)
                print_maze(maze, N, M)
            elif option == 2:
                remove_obstacle(maze, N, M)
                print_maze(maze, N, M)
            elif option == 3:
                break
            else:
                print("Invalid option. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
