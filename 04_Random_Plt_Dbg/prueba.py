import numpy as np
a = np.array([0]*5)
print (a)

#a = np.arange(1,21,2)
#b = np.linspace(1, 19, num = 10, dtype=np.int64)

#arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
#c = np.sort(arr)

# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# print (np.concatenate((a, b)))
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])
# print (np.concatenate((x, y), axis=0))

# array_ejemplo = np.array([[[0, 1, 2, 3],
#                             [4, 5, 6, 7]],
#                            [[0, 1, 2, 3],
#                             [4, 5, 6, 7]],
#                            [[0 ,1 ,2, 3],
#                             [4, 5, 6, 7]]])
# print(array_ejemplo.ndim)
# print(array_ejemplo.shape)
# print(array_ejemplo.size)

# a = np.arange(6)
# print(a)
# b = a.reshape(2, 3)
# print(b)

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a.shape)
# vec_fila = a[np.newaxis, :]
# print(vec_fila)
# vec_col = a[:, np.newaxis]
# print(vec_col)

# data = np.array([1, 2, 3])
# print(data[1])
# print(data[0:2])
# print(data[-2:])

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[a < 5])
# five_up = (a >= 5)
# print(a[five_up])
# pares = a[a%2==0]
# print(pares)
# c = a[(a > 2) & (a < 11)]
# print (c)

