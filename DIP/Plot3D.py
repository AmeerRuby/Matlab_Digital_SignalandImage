# import sys
# import os.path
import numpy
import csv
# import matplotlib as plt
import matplotlib.pyplot as pl

__author__ = "Pierre Poulain"
__credits__ = ["Justine Guegan", "Edithe Selwa", "Steven C. Howell"]
__license__ = "GPL"
# Modify for DIP course by H D Duan, July 2021

L = 3  # define the half-size of the coordinate box
v_angle = 30
azimuth = 50  # view angle and azimuth of the coordinate axes
sc = 3  # scale the vectors for clarity (presently not used)
fname = "xyz.txt"  # coordinates of points


def read_xyz(fname):
    """
    Reads coordinates from a .txt file.
    Parameters
    ----------
    fname : str
        Name of txt file.
    Returns
    -------
    array of coordinates
        [[x1 y1 z1]
         [x2 y2 z2]
         [.. .. ..]
         [xn yn zn]]
    """
    xyz = []
    with open(fname, 'r') as ff:
        rr = csv.reader(ff)
        xyz = list(rr)

    return xyz


#
# start program
#
if __name__ == '__main__':

    # --------------------------------------------------------------------------
    # compute principal axes
    # --------------------------------------------------------------------------
    # read xyz
    xyz = read_xyz(fname)

    print("%d items found in %s" % (len(xyz), fname))

    # print(xyz)

    # create coordinates array
    coord = numpy.array(xyz, float)
    d = len(coord)

    # compute geometric center
    center = numpy.mean(coord, 0)
    print("Coordinates of the geometric center:\n", center)

    # centered with geometric center
    coord = coord - center

    # compute principal axis matrix
    inertia = numpy.dot(coord.transpose(), coord)
    e_values, e_vectors = numpy.linalg.eig(inertia)
    # warning eigen values are not necessary ordered!
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html
    print("(Unordered) eigen values:")
    print(e_values)
    print("(Unordered) eigen vectors:")
    print(e_vectors)

    # --------------------------------------------------------------------------
    # order eigen values (and eigen vectors)
    #
    # axis1 is the principal axis with the biggest eigen value (eval1)
    # axis2 is the principal axis with the second biggest eigen value (eval2)
    # axis3 is the principal axis with the smallest eigen value (eval3)
    # --------------------------------------------------------------------------
    order = numpy.argsort(e_values)
    eval3, eval2, eval1 = e_values[order]
    axis3, axis2, axis1 = e_vectors[:, order].transpose()
    print("Inertia axis are now ordered !")

    # --------------------------------------------------------------------------
    print("\nFirst principal axis (in red)")
    print("coordinates: ", axis1)
    print("eigen value: ", eval1)

    print("\nSecond principal axis (in green)")
    print("coordinates:", axis2)
    print("eigen value:", eval2)

    print("\nThird principal axis (in blue)")
    print("coordinates:", axis3)
    print("eigen value:", eval3)

    # set the axies and the origin and the scope
    start = [0, 0, 0]
    fig = pl.figure()
    aa = pl.axes(projection='3d')
    aa.set_xlim([-L, L]), aa.set_ylim([-L, L]), aa.set_zlim([-L, L])
    aa.set_xlabel('X'), aa.set_ylabel('Y'), aa.set_zlabel('Z')
    aa.set_title('3D plot of ' + str(d) + ' points and eigenvectors')

    # plot 3 eigenvectors and set view perspective
    aa.quiver(start[0], start[1], start[2], axis1[0], axis1[1], axis1[2], color='r')
    aa.quiver(start[0], start[1], start[2], axis2[0], axis2[1], axis2[2], color='g')
    aa.quiver(start[0], start[1], start[2], axis3[0], axis3[1], axis3[2], color='b')
    aa.view_init(v_angle, azimuth)

    # plot the data points (in 3D), d being the number of points
    x, y, z = [0] * d, [0] * d, [0] * d
    for k in range(d):
        x[k], y[k], z[k] = coord[k, 0], coord[k, 1], coord[k, 2]
    aa.scatter(x, y, z, color='y')
"""
    V = numpy.array([axis1, axis2, axis3])
    origin = numpy.array([[0, 0, 0],[0, 0, 0]]) # origin point
    aa.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=sc)
"""
pl.show()

