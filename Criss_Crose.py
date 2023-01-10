field = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]
# raise TypeError("You dump.")


def input_for_cross():
    while True:
        string = input("Enter a position for the cross: ")
        if string.lower() == "exit":
            exit(0)
        try:
            x, y = map(int, string.split(','))
        except ValueError:
            print("Incorrect input!")
            continue
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Incorrect input!")
            continue
        if field[x - 1][y - 1] == '_':
            field[x - 1][y - 1] = 'x'
        else:
            print("Fail")
            continue

        return


def input_for_zero():
    while True:
        string = input("Enter a position for the zero: ")
        if string.lower() == "exit":
            exit(0)
        try:
            x, y = map(int, string.split(','))
        except ValueError:
            print("Incorrect input!")
            continue
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Incorrect input!")
            continue
        if field[x - 1][y - 1] == '_':
            field[x - 1][y - 1] = 'o'
        else:
            print("Fail")
            continue

        return


def check_win(arg):
    for i in range(3):
        if field[i][0] == arg and field[i][1] == arg and field[i][2] == arg:
            print(f"{arg.upper()} WIN!")
            input("Press enter for exit: ")
            exit(0)
        if field[0][i] == arg and field[1][i] == arg and field[2][i] == arg:
            print(f"{arg.upper()} WIN!")
            input("Press enter for exit: ")
            exit(0)
    if field[0][0] == arg and field[1][1] == arg and field[2][2] == arg:
        print(f"{arg.upper()} WIN!")
        input("Press enter for exit: ")
        exit(0)
    if field[0][2] == arg and field[1][1] == arg and field[2][0] == arg:
        print(f"{arg.upper()} WIN!")
        input("Press enter for exit: ")
        exit(0)
    if '_' not in field[0] and '_' not in field[1] and '_' not in field[2]:
        print("DRAW!")
        input("Press enter for exit: ")
        exit(0)


def draw():
    print("0  1  2  3")
    for i in range(3):
        print(f"{i + 1}  {field[i][0]}  {field[i][1]}  {field[i][2]}")


count = 0
while True:
    draw()
    check_win('o')
    input_for_cross()
    draw()
    check_win('x')
    input_for_zero()
