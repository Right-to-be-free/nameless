#bar plots
#To compare categorical data or show differences between groups.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
data = pd.DataFrame({"rishi": [100, 200, 300, 400], "sai": [200, 300, 400, 500], "sri": [300, 400, 500, 600]}, index=[1, 2, 3, 4])

data.plot(kind='bar')

plt.show()