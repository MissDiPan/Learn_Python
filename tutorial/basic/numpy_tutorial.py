import numpy as np


def array_t():
    a = np.array([1, 2, 3])
    print(type(a), a.shape, a[0], a[1], a[2])
    a[0] = 5
    print(a)

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    print(b.shape)
    print(b[0, 0], b[0, 1], b[1, 0])

    a = np.zeros((2, 2))
    print(a)

    b = np.ones((1, 2))
    print(b)

    c = np.full((2, 2), 7)
    print(c)

    d = np.eye(2)
    print(d)

    e = np.random.random((2, 2))
    print(e)


def array_1():
    c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    b = c[:2, 1:3]
    print(b)
    print(c[0, 1])
    b[0, 0] = 77
    print(c[0, 1])  # b and c are changed at the same time

    row_r1 = c[1, :]  # one dimension
    row_r2 = c[1:2, :]  # two dimensions
    row_r3 = c[[1], :]
    print(row_r1, row_r1.shape)
    print(row_r2, row_r2.shape)
    print(row_r3, row_r3.shape)

    col_r1 = c[:, 1]
    col_r2 = c[:, 1:2]
    print(c)
    print()  # space line
    print(col_r1, col_r1.shape)
    print(col_r2, col_r2.shape)

    a = np.array([[1, 2], [3, 4], [5, 6]])
    print(a[[0, 1, 2], [0, 1, 0]])  # row and col
    print(np.array([a[0, 0], a[1, 1], a[2, 0]]))
    print(a[[0, 0], [1, 1]])  # reuse the same element
    print(np.array([a[0, 1], a[0, 1]]))


def array_2():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    b = np.array([0, 2, 0, 1])
    print(a[np.arange(4), b])

    a[np.arange(4), b] += 10
    print(a)

    a = np.array([[1, 2], [3, 4], [5, 6]])
    bool_idx = (a > 2)
    print(bool_idx)
    print(a[bool_idx])
    print(a[a > 2])


def array_3():
    x = np.array([1, 2])
    y = np.array([1.0, 2.0])
    z = np.array([1, 2], dtype=np.int64)
    print(x.dtype, y.dtype, z.dtype)

    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)
    print(x + y)
    print(np.add(x, y))
    print(x - y)
    print(np.subtract(x, y))
    print(x * y)
    print(np.multiply(x, y))
    print(x / y)
    print(np.divide(x, y))
    print(np.sqrt(x))

    v = np.array([9, 10])
    w = np.array([11, 12])
    print(v.dot(w))
    print(np.dot(v, w))
    print(v @ w)
    print(x.dot(v))
    print(np.dot(x, v))
    print(x @ v)
    print(x.dot(y))
    print(np.dot(x, y))
    print(x @ y)

    x = np.array([[1, 2], [3, 4]])
    print(np.sum(x))
    print(np.sum(x, axis=0))
    print(np.sum(x, axis=1))
    print('transpose\n', x.T)


def broad_cast_t():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = np.empty_like(x)
    for i in range(4):
        y[i, :] = x[i, :] + v
    print(y)

    vv = np.tile(v, (4, 1))  # repeat
    print(vv)

    y = x + vv
    print(y)

    y = x + v
    print(y)

    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v
    print(y)

    v = np.array([1, 2, 3])
    w = np.array([4, 5])
    print(np.reshape(v, (3, 1)) * w)

    x = np.array([[1, 2, 3], [4, 5, 6]])
    print(x + v)
    print((x.T + w).T)
    print(x + np.reshape(w, (2, 1)))


broad_cast_t()
