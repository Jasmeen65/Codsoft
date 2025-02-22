import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Determine the winner based on the choices."""
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

def play_game():
    """Main function to play Rock-Paper-Scissors."""
    user_score, computer_score, ties = 0, 0, 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        if result == "win":
            print("🎉 You win this round!")
            user_score += 1
        elif result == "lose":
            print("😢 You lose this round!")
            computer_score += 1
        else:
            print("🤝 It's a tie!")
            ties += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    play_game()
