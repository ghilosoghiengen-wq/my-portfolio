import numpy as np

x = np.linspace(0, 10, 10)  # قيم موجبة فقط
f = np.sqrt(x**2 + 10) * np.sin(x) + np.exp(-x/5)

print(f)
