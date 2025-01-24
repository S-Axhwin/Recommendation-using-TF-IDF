import numpy as np


A = np.array([[2, 1], [3, -1]])  
b = np.array([5, 4])             


solution = np.linalg.solve(A, b)


x = solution[0]
y = solution[1]

print(f"Solution:")
print(f"x = {x}")
print(f"y = {y}")
