import numpy as np

def conv_table(x, h):
    L_x = len(x)
    L_h = len(h)
    L_y = L_x + L_h - 1
    y = np.zeros(L_y)
    for m in range(L_x):
        for n in range(L_h):
            y[m+n] += h[n]*x[m]
    return L_y, y

def lti_form(x, h):
    L_x = len(x)
    L_h = len(h)
    L_y = L_x + L_h - 1

    h1 = np.zeros(L_y)
    h1[:L_h] = h

    xh = np.zeros((L_x, L_y))
    for m in range(L_x):
        for n in range(L_y):
            xh[m,n] = h1[n]*x[m]
        h1[1:] = h1[:-1]
        h1[0] = 0

    y = np.zeros(L_y)
    for i in range(L_y):
        y[i] = sum(xh[:,i])
    return L_y, y

def overlap_addblock(x, h):
    L_x = len(x)
    L_h = len(h)
    L_y = L_x + L_h - 1

    bl_elements = int(input('Input number of elements in 1 block: '))
    bl_num = np.ceil(L_x/bl_elements).astype(int)
    bl_matrix = np.zeros((bl_num, bl_elements))
    for i in range(bl_num):
        for k in range(bl_elements):
            if (i-1)*bl_elements+k < L_x:
                bl_matrix[i,k] = x[(i-1)*bl_elements+k]

    bl_cell = [bl_matrix[i,:] for i in range(bl_num)]

    xh = [np.zeros(L_y) for _ in range(bl_num)]

    for i in range(bl_num):
        for m in range(bl_elements):
            for n in range(L_h):
                xh[i][m+n] += h[n]*bl_cell[i][m]

        if i > 0:
            q = xh[i]
            a = (i-1)*bl_elements
            for x in range(len(xh[i])):
                if x <= a:
                    q[x] = 0
                else:
                    q[x] = xh[i][x-a]
            xh[i] = q

    y = np.zeros(L_y)
    for i in range(L_y):
        for k in range(bl_num):
            y[i] += xh[k][i]
    return L_y, y

h = np.array([2, 3, 0, -5, 2, 1])
x = np.array([3, 11, 7, 0, -1, 44, 2])

L_y1, y1 = conv_table(x, h)
L_y2, y2 = lti_form(x, h)
L_y3, y3 = overlap_addblock(x, h)
y4 = np.convolve(x, h)

print(y1)
print(y2)
print(y3)
print(y4)
