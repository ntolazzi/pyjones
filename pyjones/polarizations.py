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
    eps = 1e-15

    def __init__(self, polarization, normalize=True, normal_form=True):
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
        if normal_form:
            self._make_normal_form()
        #  truncation for small values
        for idx, num in enumerate([self.Ex, self.Ey]):
            new_real = num.real
            new_imag = num.imag
            if abs(new_real) < JonesVector.eps:
                new_real = 0.0
            if abs(new_imag) < JonesVector.eps:
                new_imag = 0.0
            self[idx] = new_real+1j*new_imag

    def __repr__(self):
        return 'JonesVector([%s, %s])' % (self.polarization_vector[0, 0], self.polarization_vector[0, 1])

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Needs to be integer')
        elif item not in [0, 1]:
            raise IndexError('Index can be either 0 or 1')
        else:
            return self.polarization_vector[0, item]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('Needs to be integer')
        elif key not in [0, 1]:
            raise IndexError('Index can be either 0 or 1')
        elif not isinstance(value, (int, float, complex)):
            raise ValueError('Value needs to be numeric')
        else:
            self.polarization_vector[0, key] = value

    def _normalize(self):
        self.polarization_vector /= np.sqrt(self.intensity)

    def _make_normal_form(self):
        E_x_abs = np.abs(self.Ex)
        E_y_abs = np.abs(self.Ey)
        phi_x = np.angle(self.Ex)
        phi_y = np.angle(self.Ey)
        phi_y_rotated = phi_y - phi_x
        E_x_new = E_x_abs * np.exp(1j*0)
        E_y_new = E_y_abs * np.exp(1j*phi_y_rotated)
        self[0] = E_x_new
        self[1] = E_y_new


    @property
    def intensity(self):
        """Property which returns the intensity of the Jones vector

        :return: The intensity of the Jones vector
        :rtype: float
        """
        return np.sum(np.square(np.abs(self.polarization_vector)))

    @property
    def Ex(self):
        """Property which returns the x component of the electric field

        :return: The x component of the electric field
        :rtype: complex
        """
        return self[0]

    @property
    def Ey(self):
        """Property which returns the y component of the electric field

        :return: The y component of the electric field
        :rtype: complex
        """
        return self[1]

    @property
    def Stokes(self):
        """Property which returns the Stokes parameter representation of the Polarization

        :return: Stokes parameters
        :rtype: tuple
        """
        S0 = self.intensity
        S1 = np.abs(self.Ex) ** 2 - np.abs(self.Ey) ** 2
        S2 = 2 * np.real(self.Ex * np.conjugate(self.Ey))
        S3 = -2 * np.imag(self.Ex * np.conjugate(self.Ey))
        return S0, S1, S2, S3


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
