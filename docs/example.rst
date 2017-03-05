The following code snippet shows a classic example of the suprising effects of
light polarization::

    from pyjones.polarizations import LinearHorizontal
    from pyjones.opticalelements import Polarizer, PolarizerVertical

    input_polarization = LinearHorizontal()
    output_polarization = PolarizerVertical()*input_polarization
    print("Output: %s, Intensity: %.1f" %(output_polarization, output_polarization.intensity))
    >>> Output: JonesVector([0j, 0j]), Intensity: 0.0

    output_polarization = PolarizerVertical()*Polarizer(45)*input_polarization
    print("Output: %s, Intensity: %.1f" %(output_polarization, output_polarization.intensity))
    >>> Output: JonesVector([xx, xx]), Intensity: x.x

