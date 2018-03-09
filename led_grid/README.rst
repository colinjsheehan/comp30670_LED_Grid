========
LED_Grid
========


.. image:: https://img.shields.io/pypi/v/led_grid.svg
        :target: https://pypi.python.org/pypi/led_grid

.. image:: https://img.shields.io/travis/colinjsheehan/led_grid.svg
        :target: https://travis-ci.org/colinjsheehan/led_grid

.. image:: https://readthedocs.org/projects/led-grid/badge/?version=latest
        :target: https://led-grid.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/colinjsheehan/led_grid/shield.svg
     :target: https://pyup.io/repos/github/colinjsheehan/led_grid/
     :alt: Updates



The Science Centre is installing a new display board which is constructed from LED lights.

     The board is a square grid of LEDs which we control by sending commands to the unit to turn on or off certain rectangular regions.
     The L × L lights can be modelled as a 2 dimensional grid with L rows of lights and L lights in each row and the LED's at each corner are (0, 0), (0, L−1), (L−1, L−1) and (L − 1, 0).
     The lights are either on or off.
     Your job is to test the lights. We test them by sending instructions to turn on, turn off, or switch various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
     For example:

     • "turn on 0,0 through 999,999" would turn on (or leave on) every light.

     • "switch 0,0 through 999,0" would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.

     • "turn off 499,499 through 500,500" would turn off (or leave off) the middle four lights.

* Free software: MIT license
* Documentation: https://led-grid.readthedocs.io.


Features
--------

*  install the software 
*  enter the following argument into the command line: led_grid --input http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt
*  a local text file containing a series of commands can also be used as an input

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
