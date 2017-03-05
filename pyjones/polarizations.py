"""This module provides Jones vectors as a two dimensional representation of the polarization of light.
The basic class is JonesVector from which all predefined polarizations inherit from. Predefined polarizations are:

* LinearHorizontal
* LinearVertical
* LinearDiagonal
* LinearAntiDiagonal
* Linear(angle)
* CircularRight
* CircularLeft

"""

from __future__ import print_function
import numpy as np


class JonesVector(object):

    def __init__(self, polarization, normalize=True):
        """This represents a Jones vector and is one representation of the polarisation of light.

        :param polarization: An two element iterable with complex numbers representing the value and phase
                             of the Ex and Ey light component
        """
        if hasattr(polarization, '__iter__'):
            if len(polarization) != 2:
                raise ValueError('Length of vector/list must be excactly 2')
            else:
                self.polarization_vector = np.matrix(np.array(polarization).astype(complex))
        else:
            raise ValueError('Parameter must be either a list or a numpy.array')
        if normalize:
            self._normalize()

    def __repr__(self):
        return 'JonesVector([%s, %s])' % (self.polarization_vector[0, 0], self.polarization_vector[0, 1])

    def _normalize(self):
        self.polarization_vector /= np.sqrt(self.intensity)

    @property
    def intensity(self):
        """Property which returns the intensity of the Jones vector

        :return: The intensity of the Jones vector
        :rtype: float
        """
        return np.sum(np.square(np.abs(self.polarization_vector)))


class LinearHorizontal(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to linear horizontal polarisation"""

        super(LinearHorizontal, self).__init__([1.0, 0.0])


class LinearVertical(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to linear vertical polarisation"""

        super(LinearVertical, self).__init__([0.0, 1.0])

class Linear(JonesVector):
    def __init__(self, angle):
        """This is a subclass of JonesVector corresponding to a linear polarization with angle

        :param angle: Angle of the linear polarization with respect to horizontal plane
        """

        angle = np.radians(angle)
        super(Linear, self).__init__([np.cos(angle), np.sin(angle)])

class LinearDiagonal(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to linear diagonal polarisation"""

        super(LinearDiagonal, self).__init__([1.0, 1.0])


class LinearAntidiagonal(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to linear antidiagonal polarisation"""

        super(LinearAntidiagonal, self).__init__([1.0, -1.0])


class CircularRight(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to right circular polarisation"""

        super(CircularRight, self).__init__([1.0, -1.0j])


class CircularLeft(JonesVector):
    def __init__(self):
        """This is a subclass of JonesVector corresponding to left circular polarisation"""

        super(CircularLeft, self).__init__([1.0, 1.0j])
