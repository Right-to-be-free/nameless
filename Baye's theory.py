# Bayes' Theorem Calculation for Medical Diagnosis Example

# Given probabilities
P_D = 0.01  # Prior: Probability of having the disease
P_T_given_D = 0.9  # Likelihood: Probability of testing positive if diseased
P_T_given_not_D = 0.05  # False positive rate: Probability of testing positive if not diseased
P_not_D = 1 - P_D  # Probability of not having the disease

# Compute the total probability of testing positive (Marginal Probability)
P_T = (P_T_given_D * P_D) + (P_T_given_not_D * P_not_D)

# Compute posterior probability: P(D | T) - Probability of actually having the disease if tested positive
P_D_given_T = (P_T_given_D * P_D) / P_T

# Display results
print(P_D_given_T)
