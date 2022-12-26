side = int(input('Size of square side: '))

sides = [side]
mutable_side = side - 1
while mutable_side > 0:
    sides.extend([mutable_side] * 2)
    mutable_side -= 1

matrix = [[' ' for x in range(0, side)] for x in range(0, side)]


direction = 1
value = 1
x_coord = 0
y_coord = 0

for y in sides:
    if direction == 1:
        while y > 0:
            matrix[y_coord][x_coord] = value
            value += 1
            x_coord += 1
            y -= 1
        direction = 2
        y_coord += 1
        x_coord -= 1
    elif direction == 2:
        while y > 0:
            matrix[y_coord][x_coord] = value
            value += 1
            y_coord += 1
            y -= 1
        direction = 3
        x_coord -= 1
        y_coord -= 1
    elif direction == 3:
        while y > 0:
            matrix[y_coord][x_coord] = value
            value += 1
            x_coord -= 1
            y -= 1
        direction = 4
        y_coord -= 1
        x_coord += 1
    elif direction == 4:
        while y > 0:
            matrix[y_coord][x_coord] = value
            value += 1
            y_coord -= 1
            y -= 1
        direction = 1
        y_coord += 1
        x_coord += 1


for x in matrix:
    for _ in x:
        print(_, end=' ')
    print()

