import random
import pygame

visited = []
box_coor = 31


def get_neighbours(cell):
    left = (cell[0] - 2, cell[1])
    right = (cell[0] + 2, cell[1])
    up = (cell[0], cell[1] - 2)
    down = (cell[0], cell[1] + 2)
    neighbours = []
    if left[0] > 0:
        neighbours.append(left)
    if right[0] < 30:
        neighbours.append(right)
    if up[1] > 0:
        neighbours.append(up)
    if down[1] < 30:
        neighbours.append(down)
    return neighbours


def get_unvisited_neighbours(cell):
    return [elem for elem in get_neighbours(cell) if elem not in visited]


def is_has_unvisited_neighbours(cell):
    return len(get_unvisited_neighbours(cell)) > 0


def generate_template():
    l = []
    for q in range(31):
        if q % 2 == 0:
            a = [1] * 31
        else:
            a = [c % 2 for c in range(1, 32)]
        l.append(a)
    l[1][1] = 2
    l[19][19] = 3
    return l


def lab_generate():
    current = (1, 1)

    random.seed()
    l = generate_template()
    stack = []
    visited.append(current)
    while len(visited) < 225:
        if is_has_unvisited_neighbours(current):
            stack.append(current)
            unbrs = get_unvisited_neighbours(current)
            ind = random.randint(0, len(unbrs) - 1)
            wall_x = (unbrs[ind][0] + current[0]) // 2
            wall_y = (unbrs[ind][1] + current[1]) // 2
            l[wall_x][wall_y] = 0
            current = unbrs[ind]
            visited.append(current)
        else:
            current = stack[-1]
            stack.remove(current)
    return l


pygame.init()
screen = pygame.display.set_mode((1026, 1026))

done = False
x = 1
y = 1
labyrinth = lab_generate()

complete = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if labyrinth[x][y - 1] != 1:
            isWin = False
            if labyrinth[x][y - 1] == 3:
                isWin = True
            labyrinth[x][y - 1] = 2
            labyrinth[x][y] = 0
            y -= 1
            if isWin:
                    done = True
    if pressed[pygame.K_DOWN]:
        if labyrinth[x][y + 1] != 1:
            isWin = False
            if labyrinth[x][y + 1] == 3:
                isWin = True
            labyrinth[x][y + 1] = 2
            labyrinth[x][y] = 0
            y += 1
            if isWin:
                done = True
    if pressed[pygame.K_LEFT]:
        if labyrinth[x - 1][y] != 1:
            isWin = False
            if labyrinth[x - 1][y] == 3:
                isWin = True
            labyrinth[x - 1][y] = 2
            labyrinth[x][y] = 0
            x -= 1
            if isWin:
                done = True
    if pressed[pygame.K_RIGHT]:
        if labyrinth[x + 1][y] != 1:
            isWin = False
            if labyrinth[x + 1][y] == 3:
                isWin = True
            labyrinth[x + 1][y] = 2
            labyrinth[x][y] = 0
            x += 1
            if isWin:
                done = True

    screen.fill((0, 0, 0))
    color = ()
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 20, 20))

    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 0:
                color = (0, 0, 0)
            if labyrinth[i][j] == 2:
                image_surf = pygame.image.load("player.png").convert()

                screen.blit(image_surf, (box_coor * i, box_coor * j))

            elif labyrinth[i][j] == 1:

                _block_surf = pygame.image.load("block.png").convert()
                screen.blit(_block_surf, (box_coor * i, box_coor * j))
            elif labyrinth[i][j] == 3:

                _block_surf = pygame.image.load("door2.png").convert()
                screen.blit(_block_surf, (box_coor * i, box_coor * j))

    pygame.display.flip()
