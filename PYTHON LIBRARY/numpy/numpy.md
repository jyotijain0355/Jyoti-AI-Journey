🔹 1. What is NumPy?

NumPy (Numerical Python) ek powerful Python library hai jo numerical computing ke liye use hoti hai.

👉 Key Points:

Large data handle karta hai
Fast mathematical operations
N-dimensional arrays provide karta hai

✅ Shortcut line (Exam ke liye):
NumPy = Fast Calculation + Efficient Data Handling

🔹 2. Why NumPy is Needed?

👉 Python list ke problems:

Slow hoti hai
Manual loops use karne padte hain
Memory inefficient hoti hai

👉 NumPy solution:

Fast (vectorization)
Less memory use
Easy operations
🔹 3. Arrays in NumPy
import numpy as np

a = np.array([1,2,3])
np.zeros(3)
np.ones(3)
np.arange(0,10)
🔹 4. Properties of Array
shape → size (rows, cols)
ndim → dimension
size → total elements
dtype → data type
🔹 5. Indexing & Slicing
a[0]
a[1:4]
a[:,1]
🔹 6. Operations
a + b
a - b
a * b
np.sum(a)
np.mean(a)
🔹 7. Reshaping
a.reshape(2,2)
a.flatten()
a.ravel()
🔹 8. Iteration
for i in a:
    print(i)

np.nditer(a)
np.ndenumerate(a)
🔹 9. Copy vs View
b = a.copy()   # new memory
c = a.view()   # same memory
🔹 10. Stacking & Splitting
np.vstack()
np.hstack()
np.split()
🔹 11. Random Functions
np.random.rand()
np.random.randint()
np.random.seed()
🔹 12. Broadcasting

👉 Different size arrays ko automatically match karke operation karna

🔹 13. Advanced Indexing
Fancy indexing
Boolean indexing