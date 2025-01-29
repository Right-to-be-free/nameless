def pmf(values, probabilities, x):
    """
    Computes the Probability Mass Function (PMF) for a discrete random variable.
    
    :param values: List of possible values of the random variable.
    :param probabilities: Corresponding probabilities for each value.
    :param x: The value for which PMF is to be computed.
    :return: Probability of x if x is in values, otherwise 0.
    """
    if x in values:
        return probabilities[values.index(x)]
    return 0  # If x is not in the distribution, probability is 0.

# Example usage:
values = [1, 2, 3, 4, 5, 6]  # Outcomes of a fair die
probabilities = [1/6] * 6  # Equal probability for each outcome

print(pmf(values, probabilities, 3))  # Output: 0.1666 (1/6)
print(pmf(values, probabilities, 7))  # Output: 0 (since 7 is not a valid outcome)
