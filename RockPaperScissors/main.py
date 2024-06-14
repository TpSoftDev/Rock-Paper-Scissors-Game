import random
#Test 1

def play():
    """
    Function to play a game of Rock, Paper, Scissors.
    
    Prompts the user to input their choice and compares it with the computer's random choice.
    Returns the result of the game.

    Returns:
        str: A message indicating the computer's choice and whether the user won, lost, or tied.
    """
    print("Welcome to Rock Paper Scissors!")
    user = input("What's your choice? (R) for rock, (P) for paper, (S) for scissors\n").lower()
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return f"Computer choice is {computer}. It's a Tie!"

    if is_win(user, computer):
        return f"Computer choice is {computer}. You Won!"

    return f"Computer choice is {computer}. You Lost!"

def is_win(player, opponent):
    """
    Function to check if the player beats the opponent.

    Args:
        player (str): The player's choice ('r' for rock, 'p' for paper, 's' for scissors).
        opponent (str): The opponent's (computer's) choice.

    Returns:
        bool: True if the player wins, False otherwise.
    """
    # Return True if the player wins
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

if __name__ == "__main__":
    print(play())
