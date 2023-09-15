import numpy as np
import random as rd
import matplotlib.pyplot as pl
from scipy import stats
import time

L = 30  # define the length of number sequence
Lim = 2  # set limit for length of the axes
sc = 5  # scale the length of vector for plotting clarity
# you can change these two constants

# main
#
# generate 2 random sequences of length L
x = [0] * L
y = [0] * L
coord = []

for k in range(L):
    r = (rd.random() - 0.5) * Lim
    x[k] = r

s = time.time()  # reset the random generator
# s=round(s)%L
rd.seed(s)

for k in range(L):
    r = (rd.random() - 0.5) * Lim
    y[k] = r

# form the list of coordinates
for k in range(L):
    cc = []
    a = x[k]
    cc.append(a)
    b = y[k]
    cc.append(b)

    coord.append(cc)

print(x, '\n'), print(y, '\n')
print(coord)

# calculate Pearson correlation number and level of significance
pp, ss = stats.pearsonr(x, y)

fig = pl.figure()
aa = pl.axes()
aa.set_xlim([-Lim, Lim])
aa.set_ylim([-Lim, Lim])
aa.set_xlabel('X')
aa.set_ylabel('Y')
aa.set_title(
    "Data points and their eigenvectors" + "\nPearson correlation: " + str(pp)[0:7] + ", Significance: " + str(ss)[0:7])

# Plot the data points, color="cyan"
aa.scatter(x, y, color='c')

# the center of mass of dataset
centroid = [np.mean(x), np.mean(y)]
print(centroid)

# plot the center of mass
aa.scatter(centroid[0], centroid[1], color='r')

# calculate eigenvalues and eigenvectors
#
ncoord = np.array(coord) - centroid

inertia = np.dot(ncoord.transpose(), coord)
e_values, e_vectors = np.linalg.eig(inertia)
# warning eigen values are not necessary ordered!

print("(Unordered) eigen values:")
print(e_values)
print("(Unordered) eigen vectors:")
print(e_vectors)

# --------------------------------------------------------------------------
# order eigen values (and eigen vectors)
#
# axis1 is the principal axis with the biggest eigen value (eval1)
# axis2 is the principal axis with the second biggest eigen value (eval2)
# --------------------------------------------------------------------------
order = np.argsort(e_values)
eval2, eval1 = e_values[order]
axis2, axis1 = e_vectors[:, order].transpose()
print("Inertia axis are now ordered !")

# --------------------------------------------------------------------------
print("\nFirst principal axis (in blue)")
print("coordinates: ", axis1)
print("eigen value: ", eval1)

print("\nSecond principal axis (in green)")
print("coordinates:", axis2)
print("eigen value:", eval2)

start = np.array(centroid)
aa.quiver(start[0], start[1], axis1[0], axis1[1], color='b', scale=sc)
aa.quiver(start[0], start[1], axis2[0], axis2[1], color='g', scale=sc)
pl.show()