import random


def random_index(tokens):
    """Function to generate random index from the given list.

    Arguments:
        tokens (list)

    Returns:
        int: randomly generated index
    """
    return random.choice(range(len(tokens)))
