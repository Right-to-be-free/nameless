# Re-run the code since execution state was reset
import numpy as np
import matplotlib.pyplot as plt

# Function to compute entropy
def entropy(p):
    return -np.sum(p * np.log2(p), where=(p > 0))  # Avoid log(0) issues

# Generate probabilities for a binary system (p, 1-p)
p_values = np.linspace(0.01, 0.99, 100)  # Avoid exact 0 or 1
entropy_values = [entropy(np.array([p, 1 - p])) for p in p_values]

# Plot entropy vs. probability of one event (binary case)
plt.figure(figsize=(8, 5))
plt.plot(p_values, entropy_values, color='blue', linewidth=2)
plt.xlabel('Probability of One Event (p)')
plt.ylabel('Entropy (bits)')
plt.title('Entropy vs. Probability in a Binary System')
plt.axvline(0.5, color='red', linestyle='--', label='Max Entropy at p=0.5')
plt.legend()
plt.grid(True)
plt.show()
