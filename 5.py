import numpy as np

# Заданные значения переменных
a = 1.21
b = 0.371

# Вычисления
y = np.tan(a + b)**2 - np.sqrt(a + 1.5 + a * b**5) - b / np.log(a**2)

print(f"Значение выражения y: {y:.4f}")

