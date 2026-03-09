"""Code to create a wordle game!"""

__author__ = "730748019"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user for a guess until it matches the secret word length."""

    input_guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(input_guess) != secret_word_len:
        input_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return input_guess


def contains_char(secret_word: str, searched_char: str) -> bool:
    """Returns True if the word contains the chararcter and false if it doesn't"""
    assert len(searched_char) == 1

    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == searched_char:
            return True
        index += 1

    return False


# define the emojis
WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def emojified(input_guess: str, secret_word: str) -> str:
    """Returns emojis that will show the comparison of two strings of equal lengths, the first being the users guess and the second being the secret word"""
    assert len(input_guess) == len(secret_word)
    result: str = ""
    index: int = 0

    while index < len(secret_word):
        if input_guess[index] == secret_word[index]:
            result += GREEN_BOX
        elif contains_char(secret_word, input_guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

        index += 1

    return result


def main(secret_word: str) -> None:
    """The entrypoint of the program"""

    # State the variables
    max_turns: int = 6
    turn_number: int = 1
    won: bool = False

    while turn_number <= max_turns and not won:
        print(f"=== Turn {turn_number}/{max_turns} ===")

        # Get a valid guess
        user_guess: str = input_guess(len(secret_word))

        # Emoji result
        result_emojis: str = emojified(user_guess, secret_word)
        print(result_emojis)

        if user_guess == secret_word:
            won = True
        else:
            turn_number += 1

    # Final game results
    if won:
        print(f"You won in {turn_number}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")
