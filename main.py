side = int(input('here: '))
sides = [side]
mutable_side = side - 1

while mutable_side > 0:
    sides.extend([mutable_side] * 2)
    mutable_side -= 1

matrix = [[' ' for x in range(0, side)] for x in range(0, side)]


side_counter = 1
snake = 1
x_coord = 0
y_coord = 0

for y in sides:
    counter = y
    if side_counter == 1:
        while counter > 0:
            matrix[y_coord][x_coord] = snake
            snake += 1
            x_coord += 1
            counter -= 1
        side_counter = 2
        y_coord += 1
        x_coord -= 1
    elif side_counter == 2:
        while counter > 0:
            matrix[y_coord][x_coord] = snake
            snake += 1
            y_coord += 1
            counter -= 1
        side_counter = 3
        x_coord -= 1
        y_coord -= 1
    elif side_counter == 3:
        while counter > 0:
            matrix[y_coord][x_coord] = snake
            snake += 1
            x_coord -= 1
            counter -= 1
        side_counter = 4
        y_coord -= 1
        x_coord += 1
    elif side_counter == 4:
        while counter > 0:
            matrix[y_coord][x_coord] = snake
            snake += 1
            y_coord -= 1
            counter -= 1
        side_counter = 1
        y_coord += 1
        x_coord += 1


for x in matrix:
    for _ in x:
        print(_, end=' ')
    print()


