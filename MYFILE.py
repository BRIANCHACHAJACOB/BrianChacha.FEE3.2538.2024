import numpy as np


arrayA = np.array ([[1, 2 ],
                    [3, 4]])

arrayB = np.array ([[5, 6],
                    [7, 8]])

print(arrayA + arrayB)

#Elementwise multiplication
print(arrayA * arrayB)

#matrix product A@B
arrayC = arrayA @ arrayB
print(arrayC)