import random

class StrikeNineGame:
    def __init__(self):
        self.board = list(range(1, 10))
        self.dice = [0, 0]
        self.initialize_game()

    def initialize_game(self):
        print("\n" * 3)
        print("DO YOU NEED INSTRUCTIONS? ")
        response = input().strip().upper()
        if response == "YES":
            self.print_instructions()

        print("\nREADY TO PLAY?")
        print("\nHERE IS THE BOARD:")
        self.print_board()

    def print_instructions(self):
        print("STRIKE NINE IS PLAYED WITH A PAIR OF DICE AND A")
        print("BOARD WITH NINE NUMBERS: 1 2 3 4 5 6 7 8 9. YOU")
        print("ARE GIVEN A ROLL AND CAN KNOCK OFF UP TO 4 NUMBERS.")
        print("IF YOU INPUT THAT YOU WANT TO REMOVE 5 NUMBERS, YOU")
        print("WILL BE GIVEN A CHART OF THE NUMBERS YOU HAVE LEFT")
        print("TO REMOVE. NEXT YOU INPUT HOW MANY NUMBERS YOU WANT")
        print("TO REMOVE, AND THEN INPUT THE NUMBERS YOU WANT TO")
        print("TAKE OFF, ONE AT A TIME. THE NUMBERS YOU TAKE OFF")
        print("MUST ADD UP TO THE ROLL. YOU WIN BY REMOVING EVERY")
        print("NUMBER FROM THE BOARD. YOU LOSE IF YOU CANNOT")
        print("REMOVE ALL NUMBERS WITH THE ROLL YOU HAVE.\n")

    def print_board(self):
        print(" ".join(map(str, self.board)))

    def check_loss(self):
        if sum(self.dice) > sum(self.board):
            return True
        return False

    def check_win(self):
        if sum(self.board) == 0:
            return True
        return False

    def play(self):
        while True:
            self.dice = [random.randint(1, 6), random.randint(1, 6)]
            print("YOUR ROLL IS", sum(self.dice))

            if self.check_loss():
                print("SORRY, YOU LOST THIS TIME.")
                return

            if self.check_win():
                print("* * * CONGRATULATIONS * * *")
                print("* YOU WON *")
                return

            while True:
                num_to_remove = input("# OF NUMBERS TO REMOVE: ")
                if num_to_remove.isdigit() and 1 <= int(num_to_remove) <= 5:
                    num_to_remove = int(num_to_remove)
                    break
                else:
                    print("Please enter a valid number (1-5) or '5' to show the board.")

            if num_to_remove == 5:
                self.print_board()
                continue

            numbers_to_remove = []
            for i in range(num_to_remove):
                while True:
                    num = input(f"WHAT IS THE NUMBER {i + 1}: ")
                    if num.isdigit() and 1 <= int(num) <= 9 and self.board[int(num) - 1] not in numbers_to_remove:
                        numbers_to_remove.append(self.board[int(num) - 1])
                        break
                    else:
                        print("Invalid input. Please choose a valid number.")

            if sum(numbers_to_remove) == sum(self.dice):
                for number in numbers_to_remove:
                    self.board.remove(number)
                self.print_board()
            else:
                print("THOSE NUMBERS DON'T ADD UP TO YOUR ROLL, TRY AGAIN")


if __name__ == "__main__":
    game = StrikeNineGame()
    game.play()
