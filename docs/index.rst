.. PyJones documentation master file, created by
   sphinx-quickstart on Sat Mar  4 15:32:11 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyJones's documentation!
===================================

.. toctree::
   :maxdepth: 2


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