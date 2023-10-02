import random

print(" " * 25 + "STRIKE 9")
print(" " * 19 + "CREATIVE COMPUTING")
print(" " * 18 + "MORRISTOWN NEW JERSEY")
print("\n" * 3)


def print_board(board):
    print(" ".join(map(str, board)))


def do_you_need_instructions():
    # добавлена функция do_you_need_instructions, позволяющая узнать, нужны ли игроку инструкции.
    while True:
        user_input = input("DO YOU NEED INSTRUCTIONS (YES/NO)? ").strip().upper()
        if user_input == "YES":
            print_game_instructions()
            break
        elif user_input == "NO":
            break


def print_game_instructions():
    # добавлена функция print_game_instructions для предоставления инструкций по игре
    print("STRIKE NINE is played with a pair of dice and a board with nine numbers: 1 2 3 4 5 6 7 8 9.")
    print("You are given a roll and can knock off up to 4 numbers.")
    print(
        "Next, you input how many numbers you want to remove, and then input the numbers you want to take off, one at a time.")
    print("The numbers you take off must add up to the roll.")
    print("You win by removing every number from the board.")
    print("You lose if you cannot remove all numbers with the roll you have.\n")


def is_possible(board, current_roll):
    def helper(index, current_sum):
        if current_sum == current_roll:
            return True
        if current_sum > current_roll or index == len(board):
            return False
        include_current = helper(index + 1, current_sum + board[index])
        exclude_current = helper(index + 1, current_sum)
        return include_current or exclude_current

    return helper(0, 0)


def play():
    board = list(range(1, 10))
    do_you_need_instructions()
    print("READY TO PLAY?\n")

    while True:
        current_roll = random.randint(1, 6) + random.randint(1, 6)
        print("HERE IS THE BOARD:")
        print_board(board)
        print("YOUR ROLL IS", current_roll)

        while True:
            if current_roll is None or current_roll > 0:
                try:
                    num_to_remove = int(input("# OF NUMBERS TO REMOVE: "))
                    if num_to_remove < 1:
                        print("ANSWER 1, 2, 3, OR 4 (5 FOR THE BOARD)")
                        continue
                    elif num_to_remove > 4:
                        print("THE NUMBERS YOU HAVE LEFT TO REMOVE ARE:  ", end="")
                        print_board(board)
                        continue
                    numbers_to_remove = []

                    for _ in range(num_to_remove):
                        number = int(input("WHAT IS THE NUMBER? "))
                        if number in board:
                            numbers_to_remove.append(number)
                        else:
                            print("YOU REMOVED IT BEFORE, TRY AGAIN.")
                            break

                    if sum(numbers_to_remove) == current_roll:
                        current_roll = random.randint(1, 6) + random.randint(1, 6)
                        print("YOUR ROLL IS", current_roll)
                        for number in numbers_to_remove:
                            board.remove(number)
                    else:
                        print("THOSE NUMBERS DON'T ADD UP TO YOUR ROLL, TRY AGAIN")

                    # Check for a win condition
                    if not board:
                        print("CONGRATULATIONS! YOU WON!")
                        return True

                except ValueError:
                    print("!NUMBER EXPECTED - RETRY INPUT LINE")
                    continue

            if not is_possible(board, current_roll):
                print("SORRY, YOU LOST THIS TIME.")
                print("THE ARE", len(board), "NUMBERS LEFT ON BOARD: ", end="")
                print_board(board)
                return False


def main():
    while True:
        if not play():
            answer = input("DO YOU WANT TO TRY AGAIN (YES OR NO)? ").lower()
            if answer != "yes":
                break


if __name__ == "__main__":
    main()
