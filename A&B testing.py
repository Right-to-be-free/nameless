#A|B Testing

import scipy.stats as stats
import numpy as np

# Observed data: [Conversions, Non-Conversions]
A = np.array([200, 1000 - 200])  # Control group
B = np.array([250, 1000 - 250])  # Variant group

# Create a contingency table
table = np.array([A, B])

# Perform the Chi-Square test
chi2, p, dof, expected = stats.chi2_contingency(table)

# Output results
print(f"Chi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p:.4f}")

# Determine significance at alpha = 0.05
if p < 0.05:
    print("Statistically significant difference! Version B is better.")
else:
    print("No significant difference. Stick with Version A.")
