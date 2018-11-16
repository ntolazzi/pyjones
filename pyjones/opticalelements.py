"""This module provides optical elements which influence the polarization of light. The basic class is
JonesMatrix from which all predefined optical elements inherit from. Predefined optical elements are:

* PolarizerHorizontal
* PolarizerVertical
* Polarizer(angle)
* QuarterWavePlate(angle)
* HalfWavePlate(angle)

"""

from __future__ import print_function
from pyjones.polarizations import *


class JonesMatrix(object):
    def __init__(self, matrix):
        """This is the baseclass which describes a polarization influencing optical element.

        :param matrix: A 2x2 matrix either of type np.matrix or a list of two two-element lists describing
                       the effect of that optical element to the polarization state of passing light.
        """
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
        """The multiplication operator is overloaded to allow for multiplication of two Jones matrices as well as
        multiplication with a Jones Vector

        :param other: JonesMatrix or JonesVector with which the current instance is multiplied
        :return: JonesMatrix or JonesVector
        """
        if isinstance(other, JonesVector):
            resulting_polarisation = self.matrix * other.polarization_vector.T
            return JonesVector([resulting_polarisation[0, 0], resulting_polarisation[1, 0]], normalize=False)
        elif isinstance(other, JonesMatrix):
            return JonesMatrix(self.matrix * other.matrix)
        else:
            raise TypeError('Multiplication does only work for JonesMatrix or JonesVector')


class PolarizerHorizontal(JonesMatrix):
    def __init__(self):
        """This is a subclass of JonesMatrix corresponding to a horizontal polarizer"""

        matrix = [[1.0, 0.0], [0.0, 0.0]]
        super(PolarizerHorizontal, self).__init__(matrix)


class PolarizerVertical(JonesMatrix):
    def __init__(self):
        """This is a subclass of JonesMatrix corresponding to a vertical polarizer"""

        matrix = [[0.0, 0.0], [0.0, 1.0]]
        super(PolarizerVertical, self).__init__(matrix)


class Polarizer(JonesMatrix):
    def __init__(self, angle):
        """This is a subclass of JonesMatrix corresponding to a polarizer with angle

        :param angle: Angle of the polarizer with respect to horizontal plane
        """
        angle = np.radians(angle)
        matrix = [[np.cos(angle)**2, np.sin(angle)*np.cos(angle)], [np.sin(angle)*np.cos(angle), np.sin(angle)**2]]
        super(Polarizer, self).__init__(matrix)


class QuarterWavePlate(JonesMatrix):
    def __init__(self, angle):
        """This is a subclass of JonesMatrix corresponding to a quarter wave plate with angle

        :param angle: Angle of the fast axis of the quarter wave plate with respect to horizontal plane
        """

        angle = np.radians(angle)
        matrix = np.exp(1.0j * np.pi / 4.0) * np.matrix([[np.cos(angle) ** 2 + 1.0j * np.sin(angle) ** 2,
                                                          (1.0 - 1.0j) * np.sin(angle) * np.cos(angle)],
                                                         [(1.0 - 1.0j) * np.sin(angle) * np.cos(angle),
                                                          np.sin(angle) ** 2 + 1.0j * np.cos(angle) ** 2]])
        super(QuarterWavePlate, self).__init__(matrix)


class HalfWavePlate(JonesMatrix):
    def __init__(self, angle):
        """This is a subclass of JonesMatrix corresponding to a half wave plate with angle

        :param angle: Angle of the fast axis of the half wave plate with respect to horizontal plane
        """

        angle = 2*np.radians(angle)
        matrix = [[np.cos(angle), np.sin(angle)], [np.sin(angle), -np.cos(angle)]]
        super(HalfWavePlate, self).__init__(matrix)

class PhaseRetarder(JonesMatrix):
    def __init__(self, angle, eta):
        """This is a subclass of JonesMatrix corresponding to a quarter wave plate with angle

        :param angle: Angle of the fast axis of the quarter wave plate with respect to horizontal plane
        """

        angle = np.radians(angle)
        eta = np.radians(eta)
        matrix = np.exp(- 1.0j * eta / 2.0) * np.matrix([[np.cos(angle) ** 2 + np.exp(1j*eta) * np.sin(angle) ** 2,
                                                          (1.0 - np.exp(1j*eta)) * np.sin(angle) * np.cos(angle)],
                                                         [(1.0 - np.exp(1j*eta)) * np.sin(angle) * np.cos(angle),
                                                          np.sin(angle) ** 2 + np.exp(1j*eta) * np.cos(angle) ** 2]])
        super(PhaseRetarder, self).__init__(matrix)
