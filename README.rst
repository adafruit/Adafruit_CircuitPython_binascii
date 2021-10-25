Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-binascii/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/binascii/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_binascii/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_binascii/actions/
    :alt: Build Status

The binascii module contains a number of methods to convert between binary and various ASCII-encoded binary representations.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-binascii/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-binascii

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-binascii

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-binascii

Usage Example
=============

Hex <-> Binary Conversions

.. code-block:: python

        from adafruit_binascii import hexlify, unhexlify
        # Binary data.
        data = b"CircuitPython is Awesome!"

        # Get the hexadecimal representation of the binary data
        hex_data = hexlify(data)
        print("Hex Data: ", hex_data)

        # Get the binary data represented by hex_data
        bin_data = unhexlify(hex_data)
        print("Binary Data: ", bin_data)

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://circuitpython.readthedocs.io/projects/binascii/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_binascii/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
