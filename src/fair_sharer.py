import numpy as np

def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.

    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
    values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations
    """
    values_new = np.array(values, dtype=float)

    for _ in range(num_iterations):
        idx = int(np.argmax(values_new))
        amount = values_new[idx] * share
        values_new[idx] -= 2 * amount
        values_new[(idx - 1) % len(values_new)] += amount
        values_new[(idx + 1) % len(values_new)] += amount

    return list(values_new.astype(int))