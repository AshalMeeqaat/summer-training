"""
Task 1 — Problem 8 (Medium): The Minion Game

HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

Adapted as a function so it can be tested automatically.
"""

VOWELS = "AEIOU"


def minion_game(word: str) -> str:
    """Play the Minion Game on an uppercase word and return the result.

    Two players make substrings of `word`:
    - Kevin scores every substring that starts with a vowel (A, E, I, O, U).
    - Stuart scores every substring that starts with a consonant.

    A letter at index i in a word of length word_length starts (word_length - i) substrings.

    Return:
    - "Stuart <score>" if Stuart wins,
    - "Kevin <score>" if Kevin wins,
    - "Draw" if the scores are equal.

    Example: "BANANA" -> "Stuart 12".
    """
    stuart_score = 0
    kevin_score = 0
    word_length = len(word)

    for i in range(word_length):
        score = word_length - i

        if word[i] in VOWELS:
            kevin_score += score
        else:
            stuart_score += score

    if stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    if kevin_score > stuart_score:
        return f"Kevin {kevin_score}"

    return "Draw"


if __name__ == "__main__":
    print(minion_game("BANANA"))
