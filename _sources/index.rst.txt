.. PyJones documentation master file, created by
   sphinx-quickstart on Sat Mar  4 15:32:11 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyJones's documentation!
===================================

.. toctree::
   :maxdepth: 2

The `Jones calculus <https://en.wikipedia.org/wiki/Jones_calculus>`_ is a very convinient form for calculating the polarization of light under the influence of
polarization changing optical elements. Therefore it is possible to model a whole beampath and find out the final
polarization after multiple optical elements.
**PyJones** is ment as an easy interface for these calculations in Python and prvides several predefined polarizations
and optical elements which are commonly used.

The best way to understand how **PyJones** works is by just going through the examples and see the API. Afterwards it
is advisable to have a look at the class and module documentation below so you can find out which predefined
elements exist and how to use them.

Examples:
=========

.. include:: example.rst


************
Jones Vector
************

.. automodule:: pyjones.polarizations

**Base Class**

.. autoclass:: pyjones.polarizations.JonesVector
   :members:

**Predefined Polarizations**

.. autoclass:: pyjones.polarizations.LinearHorizontal

.. autoclass:: pyjones.polarizations.LinearVertical
.. autoclass:: pyjones.polarizations.Linear
.. autoclass:: pyjones.polarizations.LinearDiagonal
.. autoclass:: pyjones.polarizations.LinearAntidiagonal
.. autoclass:: pyjones.polarizations.CircularRight
.. autoclass:: pyjones.polarizations.CircularLeft

************
Jones Matrix
************

.. automodule:: pyjones.opticalelements

**Base Class**

.. autoclass:: pyjones.opticalelements.JonesMatrix
    :members:

**Predefined Optical Elements**

.. autoclass:: pyjones.opticalelements.PolarizerHorizontal
.. autoclass:: pyjones.opticalelements.PolarizerVertical
.. autoclass:: pyjones.opticalelements.Polarizer
.. autoclass:: pyjones.opticalelements.QuarterWavePlate
.. autoclass:: pyjones.opticalelements.HalfWavePlate