import random

def main():
    print(" " * 25 + "STRIKE 9")
    print(" " * 19 + "CREATIVE COMPUTING")
    print(" " * 18 + "MORRISTOWN NEW JERSEY")
    print("\n" * 2)

    print_instructions = input("DO YOU NEED INSTRUCTIONS (YES/NO)? ").strip().upper()

    if print_instructions == "YES":
        print_game_instructions()

    print("READY TO PLAY?\n")

    while True:
        board = list(range(1, 10))
        player_turn(board)

        play_again = input("PLAY ANOTHER GAME (YES/NO)? ").strip().upper()
        if play_again != "YES":
            break

def print_game_instructions():
    print("STRIKE NINE is played with a pair of dice and a board with nine numbers: 1 2 3 4 5 6 7 8 9.")
    print("You are given a roll and can knock off up to 4 numbers.")
    print("If you input that you want to remove 5 numbers, you will be given a chart of the numbers you have left to remove.")
    print("Next, you input how many numbers you want to remove, and then input the numbers you want to take off, one at a time.")
    print("The numbers you take off must add up to the roll.")
    print("You win by removing every number from the board.")
    print("You lose if you cannot remove all numbers with the roll you have.\n")

def player_turn(board):
    while True:
        print("HERE IS THE BOARD:")
        print_board(board)

        roll = random.randint(1, 6) + random.randint(1, 6)
        print(f"YOUR ROLL IS {roll}")

        total_on_board = sum(board)
        if roll > total_on_board:
            print("SORRY, YOU LOST THIS TIME.")
            break
        elif roll == total_on_board:
            print("* * * CONGRATULATIONS * * *")
            print("* YOU WON *\n")
            break

        num_to_remove = int(input("# OF NUMBERS TO REMOVE: "))
        if num_to_remove < 1 or num_to_remove > 4:
            print("ANSWER 1, 2, 3, OR 4 (5 FOR THE BOARD)")
            continue

        nums_to_remove = []
        print("WHAT IS THE NUMBER?")
        for _ in range(num_to_remove):
            num = int(input())
            if num not in board:
                print("YOU REMOVED IT BEFORE, TRY AGAIN.")
                break
            nums_to_remove.append(num)

        if sum(nums_to_remove) != roll:
            print("THOSE NUMBERS DON'T ADD UP TO YOUR ROLL, TRY AGAIN")
            continue

        for num in nums_to_remove:
            board.remove(num)

        print("\nNUMBERS REMOVED: ", nums_to_remove)
        print_board(board)

        print("YOU ROLL")  # Добавляем команду "YOU ROLL" после удаления чисел

def print_board(board):
    print(" ".join(map(str, board)))

if __name__ == "__main__":
    main()

