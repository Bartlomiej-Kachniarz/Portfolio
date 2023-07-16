import numpy as np

a = np.array([1, 2, 3], dtype= 'int32')
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# get dimension

print(a.ndim)
print(b.shape)

# get type
print(b.dtype)
print(a.itemsize)

# total size
print(b.size * b.itemsize)
print(b.nbytes)

# other example
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# get a specific element
print(a[1, 5])
print(a[-1, -2])

# get a specific row
print(a[0, :])
print(a[:, 2])

# getting fancy

print(a[0, 1:-1:2])

a[1, 5] = 20
print(a)

a[:, 2] = [1, 2]
print(a)

# 3D example

b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

# get a specific element
print(b[0, 1, 1])
print(b[:, 1, :])

# replace
# b[:, 1, :] = [9, 9, 9]

# all at zeros
c = np.zeros(((2, 3, 4)))
print(c)

print(np.ones((4,2,2), dtype='int32'))

# any other number

print(np.full((4,4), 99, dtype = 'float32'))

print(np.full_like(a, 4))

# random decimal numbers

print(np.random.rand(4, 2, 3))
print(np.random.random_sample(a.shape))

#random integer
print(np.random.randint(4, 7, size = (3, 3)))

# macierz jednostek identity
print(np.identity(5))

arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# training
k = 9
array = np.ones((k, k), dtype='int32')
array[1:-1, 1:-1] = np.zeros((k - 2, k - 2))
s = (k - 1)/2
s = int(s)
array[s,s] = 9
print(array)

# BE CAREFUL WHEN COPYING ARRAYS!

a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(a)
print(b)

a = np.array([1, 2, 3, 4])
print(a)

a = a ** 2
print(a)

print(np.sin(a))

# Linear ALGEBRA

a = np.ones((2,3))
print(a)

b =np.full((3,2), 2)
print(b)

print(np.matmul(a, b))
print(np.matmul(b, a))

# find the determinant
c = np.identity(3)
print(np.linalg.det(c))

# other things to do:
# trace, singular vector decomposition, eigenvalues, matrix norm, inverse, etc.

# STATISTICS

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)
print(np.min(stats))
print(np.sum(stats))
print(np.sum(stats, axis=0))

# reorganizing arrays

before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)

after = before.reshape((8,1)) # no of values must be equal
print(after)


# vertically stacking vectors

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2, v1, v2]))
print(np.hstack([v1, v2]))

# load data from file

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# advanced indexes and boolean masking

print(filedata > 50)
print(filedata[filedata > 50]) # get the indexes

# you can index with a list in NumPy
d = np.array([1,2,3,4,5,6,7,8,9])
d[[1, 2, 8]]

print(np.any(filedata > 50, axis=0))
print(np.all(filedata > 50, axis=0))

print((filedata > 50) & (filedata < 100))
print(~(filedata > 50) & (filedata < 100))

# a[2:4,0:2]
# a[1,1]




