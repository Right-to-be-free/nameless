import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parameters for the Binomial Distribution
n = 10  # Number of trials
p = 0.5  # Probability of success

# Generate possible values of X (0 to n)
x = np.arange(0, n+1)

# Compute Binomial PMF (Probability Mass Function)
pmf_values = stats.binom.pmf(x, n, p)

# Compute Binomial CMF (Cumulative Mass Function)
cmf_values = stats.binom.cdf(x, n, p)

# Plot PMF and CMF
fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# PMF Plot
ax[0].bar(x, pmf_values, color='blue', alpha=0.6, label='PMF')
ax[0].set_title('Binomial Distribution PMF (n=10, p=0.5)')
ax[0].set_xlabel('Number of Successes (X)')
ax[0].set_ylabel('Probability')
ax[0].legend()

# CMF Plot
ax[1].step(x, cmf_values, where='mid', color='red', label='CMF', linewidth=2)
ax[1].set_title('Binomial Distribution CMF (n=10, p=0.5)')
ax[1].set_xlabel('Number of Successes (X)')
ax[1].set_ylabel('Cumulative Probability')
ax[1].legend()

# Show plots
plt.tight_layout()
plt.show()
