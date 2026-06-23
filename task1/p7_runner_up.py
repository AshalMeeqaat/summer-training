"""
Task 1 — Problem 7 (Easy): Find the Runner-Up Score

HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Adapted as a function so it can be tested automatically.
"""

sample_scores = [2, 3, 6, 6, 5]


def find_runner_up(scores: list[int]) -> int:
    """Return the runner-up score: the second highest *distinct* value.

    Example: [2, 3, 6, 6, 5] -> 5 (6 is the highest, 5 is the runner-up).
    """
    # TODO: Remove duplicate scores, then return the second largest value.
    new_list = []
    for score in scores:
        if score not in new_list:
            new_list.append(score)

    new_list.sort()
    print(new_list)
    if new_list:
        return new_list[-2]
    else:
        return None

    pass


if __name__ == "__main__":
    print(find_runner_up(sample_scores))
