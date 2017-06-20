import numpy as np


""" Change the penalties here to deviate from the Levenshtein cost """
INSERTION_PENALTY = 1
DELETION_PENALTY = 1
SUBSTITUTION_PENALTY = 2
ALLOWED_LEVELS = ["word", "char"]
LEVEL = "word"


reference = "if there is no rain in April you will have a great summer"
sequences = ["no rain in april then great summer come",
             "there is rain in April you have summer",
             "in April no rain you have summer great",
             "there is no rain in apple a great summer comes",
             "you have a great summer comes if there is no rain in April"]




def compute_cost(D, i, j, token_X, token_Y):
    relative_subst_cost = 0 if token_X == token_Y else SUBSTITUTION_PENALTY
    return min(D[i-1, j] + INSERTION_PENALTY, D[i, j-1] + DELETION_PENALTY, D[i-1, j-1] + relative_subst_cost)


def tokenize_string(string, level="word"):
    assert level in ALLOWED_LEVELS
    if level is "word":
        return string.split(" ")
    else:
        return list(string)


def minimum_edit_distance(string1, string2, level="word"):
    """The function uses the dynamic programming approach from Wagner-Fischer to compute the minimum edit distance
    between two sequences.
    :param string1 first sequence
    :param string2 second sequence
    :param level defines on which granularity the algorithm shall be applied. "word" specifies the token to
    be sequential words while "char" applies the algorithm on a character-by-character level"""
    string1_tokens = tokenize_string(string1, level)
    string2_tokens = tokenize_string(string2, level)
    n = len(string1_tokens)
    m = len(string2_tokens)

    print(string2_tokens)

    D = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if j == 0:
                D[i,j] = i
            elif i == 0:
                D[i,j] = j
            else:
                D[i,j] = compute_cost(D, i, j, string1_tokens[i], string2_tokens[j])

    return D[n-1,m-1]


def main():
    for sequence in sequences:
        print(minimum_edit_distance(reference, sequence, level=LEVEL))


if __name__ == "__main__":
    main()
