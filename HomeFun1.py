def DoMove(position, move):
    return position - move

def GenerateMoves(position):
    return [1, 2] if position >= 2 else [1]

def PrimitiveValue(position):
    if position == 0:
        return 'lose'
    else:
        return 'not_primitive'

def Solve(position):
    value = PrimitiveValue(position)
    if value != 'not_primitive':
        return value

    moves = GenerateMoves(position)
    if any(Solve(DoMove(position, move)) == 'lose' for move in moves):
        return 'win'
    else:
        return 'lose'

def main():
    while True:
        try:
            position = int(input("Enter the number of pennies (0-10, or -1 to exit): "))
            if position == -1:
                break
            if 0 <= position <= 10:
                print(f"{position:02}: {Solve(position)}")
            else:
                print("Please enter a valid number of pennies (0-10).")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
