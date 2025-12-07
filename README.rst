==========
SURFACE INSTALLER
==========


.. image:: https://img.shields.io/pypi/v/weathereye.svg
        :target: https://pypi.python.org/pypi/weathereye

..
    .. image:: https://img.shields.io/travis/isedwards/weathereye.svg
            :target: https://travis-ci.com/isedwards/weathereye
    
    .. image:: https://readthedocs.org/projects/weathereye/badge/?version=latest
            :target: https://weathereye.readthedocs.io/en/latest/?version=latest
            :alt: Documentation Status


SURFACE INSTALLER Python Package and Command Line Interface (CLI) built on top of WeatherEye

* Free software: MIT license
* Documentation: https://docs.weathereye.org


Supported Operating Systems
---------------------------
Linux

* ``Ubuntu 22.04``


Install
-------

Update and Upgrade Packages

.. code-block::

    sudo apt update; sudo apt upgrade

Install pipx

.. code-block::

    sudo apt install pipx; pipx ensurepath; source ~/.bashrc

Install surface-installer

.. code-block::

    pipx install surface-installer

Run ``surface-installer``

.. code-block::

    surface install

Features
--------

Currently, the ``surface-installer`` command line tool is limited to:

* ``surface --help`` - List available available commands

* ``surface install`` - Launches a web application to install SURFACE and configure environment variables


Usage
-----

1. **Enable SSH connections for remote machines:**

* To download SURFACE on remote machines, ensure that the remote machines can be accessed via SSH.

..
    Credits
    -------
    
    This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
    
    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
