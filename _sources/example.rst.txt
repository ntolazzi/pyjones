The following code snippet shows a classic example of the surprising effects of
light polarization

.. ipython::

    In [1]: from pyjones.polarizations import LinearHorizontal

    In [2]: from pyjones.opticalelements import Polarizer, PolarizerVertical

    In [3]: input_polarization = LinearHorizontal()

    In [4]: output_polarization = PolarizerVertical()*input_polarization

    In [5]: print("Output: %s, Intensity: %.2f" %(output_polarization, output_polarization.intensity))

That means the light is perfectly blocked. We now put in one more polarizer:

.. ipython::

    In [6]: output_polarization = PolarizerVertical()*Polarizer(45)*input_polarization

    In [7]: print("Output: %s, Intensity: %.2f" %(output_polarization, output_polarization.intensity))

That means if we put in one more polarizer in the middle suddenly there is light again.

You can also use **PyJones** to visualize for example
`Malus' law <https://en.wikipedia.org/wiki/Polarizer#Malus.27_law_and_other_properties>`_ that states the the
transmitted intensity of a linear polarized beam trough a polarizer is given by

.. math::
    I \propto \cos^2(\theta)

where :math:`\theta` is the angle between the input polarization and the polarizer.


.. ipython::
    @savefig

    In [1]: import matplotlib.pyplot as plt

    In [2]: import numpy as np

    In [3]: from pyjones.polarizations import LinearHorizontal

    In [4]: from pyjones.opticalelements import Polarizer

    In [5]: angles = np.linspace(0, 360, 1000)

    In [6]: intensities = [(Polarizer(angle)*LinearHorizontal()).intensity for angle in angles]

    @savefig plot_simple.png width=4in
    In [7]: plt.plot(angles, intensities);


