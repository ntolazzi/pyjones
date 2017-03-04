"""This module provides optical elements which influence the polarization of light. The basic class is
JonesMatrix from which all predefined optical elements inherit from. Predefined optical elements are:
* PolarizerHorizontal
* PolarizerVertical
* Polarizer(angle)
* QuarterWavePlate(angle)
* HalfWavePlate(angle)
"""

from __future__ import print_function
import numpy as np
from pyjones.polarizations import *


class JonesMatrix(object):
    def __init__(self, matrix):
        if hasattr(matrix, '__iter__'):
            np_not_right_shape = True
            if isinstance(matrix, np.matrix):
                np_not_right_shape = True if matrix.shape != (2, 2) else False
            if (len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2) and np_not_right_shape:
                raise ValueError('Shape of array/matrix must be 2x2')
            else:
                self.matrix = np.matrix(matrix).astype(complex)
        else:
            raise ValueError('Parameter must be either 2x2 array or numpy.matrix')

    def __repr__(self):
        return 'JonesMatrix([[%s, %s], [%s, %s]])' % (self.matrix[0, 0], self.matrix[0, 1], self.matrix[1, 0],
                                                      self.matrix[1, 1])

    def __mul__(self, other):
        if isinstance(other, JonesVector):
            resulting_polarisation = self.matrix * other.polarization_vector.T
            return JonesVector([resulting_polarisation[0, 0], resulting_polarisation[1, 0]], normalize=False)
        elif isinstance(other, JonesMatrix):
            return JonesMatrix(self.matrix * other.matrix)


class PolarizerHoriontal(JonesMatrix):
    def __init__(self):
        matrix = [[1.0, 0.0], [0.0, 0.0]]
        super(PolarizerHoriontal, self).__init__(matrix)


class PolarizerVertical(JonesMatrix):
    def __init__(self):
        matrix = [[0.0, 0.0], [0.0, 1.0]]
        super(PolarizerVertical, self).__init__(matrix)


class Polarizer(JonesMatrix):
    def __init__(self, angle):
        matrix = [[], []]
        super(Polarizer, self).__init__(matrix)


class QuarterWavePlate(JonesMatrix):
    def __init__(self, angle):
        angle = np.radians(angle)
        matrix = np.exp(1.0j * np.pi / 4.0) * np.matrix([[np.cos(angle) ** 2 + 1.0j * np.sin(angle) ** 2,
                                                          (1.0 - 1.0j) * np.sin(angle) * np.cos(angle)],
                                                         [(1.0 - 1.0j) * np.sin(angle) * np.cos(angle),
                                                          np.sin(angle) ** 2 + 1.0j * np.cos(angle) ** 2]])
        super(QuarterWavePlate, self).__init__(matrix)


class HalfWavePlate(JonesMatrix):
    def __init__(self, angle):
        matrix = [[], []]
        super(HalfWavePlate, self).__init__(matrix)


if __name__ == '__main__':
    vec = CircularRight()
    test_eval_jv = eval(str(vec))
    print(test_eval_jv)
    mat = PolarizerHoriontal
    mat3 = QuarterWavePlate(45)
    print((mat3 * vec).intensity)
    import matplotlib.pyplot as plt

    degrees = np.linspace(0, 360, 1000)
    intensities = [(PolarizerVertical() * QuarterWavePlate(de) * vec).intensity for de
                   in degrees]
    plt.plot(degrees, intensities)
    plt.show()
