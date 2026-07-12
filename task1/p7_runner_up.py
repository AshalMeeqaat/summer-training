"""
Task 1 — Problem 7 (Easy): Find the Runner-Up Score

HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Adapted as a function so it can be tested automatically.
"""

sample_scores = [2, 3, 6, 6, 5]


def find_runner_up(scores: list[int]) -> int | None:
    """Return the runner-up score: the second highest *distinct* value.

    Example: [2, 3, 6, 6, 5] -> 5 (6 is the highest, 5 is the runner-up).
    """
    highest = None
    second_highest = None

    for score in scores:
        if highest is None or score > highest:
            second_highest = highest
            highest = score
        elif score != highest and (second_highest is None or score > second_highest):
            second_highest = score

    return second_highest


if __name__ == "__main__":
    print(find_runner_up(sample_scores))
