import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Get the screen dimensions
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.timeout(100)

# Initial snake and food settings
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]
food = [sh//2, sw//2]
special_food = [sh//4, sw//4]

# Place initial food
w.addch(food[0], food[1], 'π')
w.addch(special_food[0], special_food[1], 'X')

# Initial direction
key = curses.KEY_RIGHT

# Place obstacles
obstacles = []
for _ in range(int(sh * sw * 0.05 / 5)):
    if random.choice([True, False]):
        # Horizontal obstacle
        obs_x = random.randint(5, sw-5)
        obs_y = random.randint(1, sh-2)
        for i in range(5):
            w.addch(obs_y, obs_x+i, curses.A_REVERSE)
            obstacles.append([obs_y, obs_x+i])
    else:
        # Vertical obstacle
        obs_x = random.randint(1, sw-2)
        obs_y = random.randint(5, sh-5)
        for i in range(5):
            w.addch(obs_y+i, obs_x, curses.A_REVERSE)
            obstacles.append([obs_y+i, obs_x])

normal_food_count = 0
special_food_count = 0

# Main game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if key == ord(' '):
        # Pause and resume the game
        while w.getch() != ord(' '):
            pass
        continue

    # Calculate the new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Wrap around the screen boundaries
    new_head[0] = (new_head[0] + sh) % sh
    new_head[1] = (new_head[1] + sw) % sw

    # Check if snake collides with itself or obstacles
    if new_head in snake or new_head in obstacles:
        break

    snake.insert(0, new_head)

    # Check if snake eats normal food
    if snake[0] == food:
        normal_food_count += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake and nf not in obstacles else None
        w.addch(food[0], food[1], 'π')
    else:
        snake.pop()

    # Check if snake eats special food
    if snake[0] == special_food:
        special_food_count += 1
        special_food = None
        while special_food is None:
            sf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            special_food = sf if sf not in snake and sf not in obstacles else None
        w.addch(special_food[0], special_food[1], 'X')
        if len(snake) > 1:
            snake.pop()

    w.clear()
    for y, x in snake:
        w.addch(y, x, '#')
    w.addch(food[0], food[1], 'π')
    w.addch(special_food[0], special_food[1], 'X')
    for y, x in obstacles:
        w.addch(y, x, curses.A_REVERSE)

# End the game
curses.endwin()
print(f"Game Over! Normal food eaten: {normal_food_count}, Special food eaten: {special_food_count}")
