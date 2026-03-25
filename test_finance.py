import numpy as np
import pandas as pd

data = pd.DataFrame({
    "Returns": np.random.normal(0.01, 0.05, 1000)
})

print("Average Return:", data["Returns"].mean())
print("Volatility:", data["Returns"].std())