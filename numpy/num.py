from re import A
import numpy as np

my_arrayA = np.array([10, 20, 30, 40, 50])
my_arrayB = np.array([5, 4, 3, 2, 1])

print(my_arrayA + my_arrayB)
print(my_arrayA - my_arrayB)
print(my_arrayA * my_arrayB)
print(my_arrayA / my_arrayB)

print(my_arrayA.mean())
print(my_arrayA.max())
print(my_arrayA.min())

result = np.dot(my_arrayA, my_arrayB) 
print(result)

reshaped_array = my_arrayA.reshape(5,1) 
print(reshaped_array)
