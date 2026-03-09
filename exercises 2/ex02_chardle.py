"""EX02 - Chardle - A step towards Wordle."""

__author__ = "730748019"

main() ->
def input_word() -> str:
    """Asks the user for a 5-character word."""
    user_word: str = input("Enter a 5-character word: ")
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    """Asks the user for a single character."""
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_letter

def contains_char(word: str, letter: str) -> None:
    """Checks each index of the word for the letter."""
    print("Searching for " + letter + " in " + word)

    count: int = 0

    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
