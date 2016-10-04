.. link: 
.. description: 
.. tags: 
.. date: 2014/02/08 12:25:03
.. title: Software projects
.. slug: software

All my code is open-source (BSD- or MIT-licensed where possible) and
available on GitHub. For the most part, these are astronomy-related
libraries, though there are a couple more general statistics or signal
processing libraries.

.. raw:: html
   
   <br />

.. image:: /images/python.png
   :height: 40px
   :align: left

   
Python & C
----------

I maintain four Python packages on the `Python package index`_ and
have contributed to several others. A couple packages are mainly
written in C and these have C APIs.

====

.. image:: /images/sncosmo.png
   :height: 36px
   :align: left

`SNCosmo`_
..........

SNCosmo is a Python package for supernova cosmology data analysis and
simulation. I'm the creator and main developer. `SNCosmo on GitHub`_.

====

`SEP`_
......

SEP is a Python and C library for source detection and photometry,
adapted from the Source Extractor code base. I created it in order to
make the Source Extractor background and detection algorithms available
directly from Python. `SEP on GitHub`_.

====

`Nestle`_
.........

(Rhymes with "wrestle".) An open-source (MIT-licensed) pure-Python
implementation of nested sampling algorithms, similar to those in
the MultiNest software. `Nestle on Github`_.

====

`Extinction`_
.............

Fast (Cython-based) implementation of interstellar dust extinction
laws for Python. `Extinction on Github`_.

====

`bsplines`_
...........

Work-in-progress optimized 1-d and 2-d cubic splines in C and Python.
These can be a factor of 5 or more faster than the FORTRAN-based spline
classes in scipy.interpolate.

====

.. image:: /images/astropy.png
   :height: 36px
   :align: left

`AstroPy`_
..........

AstroPy is a community-developed Python library for astronomy.  In the
core package, I designed the logo and the layout and style for the
documentation and contributed several functions in the ``stats``
module. I wrote the initial code for the `PhotUtils`_ affiliated
package for photometry. `AstroPy on GitHub`_.

====


.. raw:: html
   
   <br /><br />


.. image:: /images/julia.png
   :height: 40px
   :align: left

Julia
-----

I maintain about six registered Julia packages on the `Julia package
index`_.

====

.. image:: /images/juliaastro.png
   :height: 36px
   :align: left

`Julia Astro`_
..............

Collection of astronomy packages for the `Julia`_ programming language.  I wrote the
bulk of the `FITSIO.jl`_ package for FITS file format I/O and also
contributed the `DustExtinction.jl`_ package for simple extinction
laws. I also maintain the WCS.jl and Cosmology.jl packages. `Julia
Astro on GitHub`_.


====

`Dierckx.jl`_
.............

Dierckx.jl is a package for 1-d and 2-d splines in Julia. It's a
wrapper of the dierckx Fortran library available from NETLIB, the same
library underlying the spline classes in scipy.interpolate.

====

`SkyCoords.jl`_
...............

Simple and fast astronomical coordinate system transformations in Julia.
Transforms between ICRS, galactic, and FK5 (e.g., J2000) coordinate systems.

====


.. raw:: html
   
   <br /><br />


.. image:: /images/snfactory.jpg
   :height: 36px
   :align: left

Nearby Supernova Factory
------------------------

I've released open-source code for the cosmology experiment that I
work on, the `Nearby Supernova Factory`_ and manage the group's GitHub
organization at http://github.com/snfactory. In addition to the code
I've written for the project, I'm working on open-sourcing legacy
components of the group's data processing pipeline to enable
reproducibility.


====

`cubefit`_
..........

Simultaneous fit of a supernova spectral time series and galaxy model
on multiple spectral data cubes. Uses some FFT tricks for a fast
analytical calculation of the gradient of the objective function,
allowing us to efficiently optimize a model with over a million
parameters (with regularization). The code is particular to snfactory
data, but open-source for anyone to inspect and adapt for their needs.

====

.. _`Python package index`: http://pypi.org
.. _`Julia package index`: http://pkg.julialang.org
.. _`Julia`: http://julialang.org
.. _`Julia Astro`: http://juliaastro.github.io
.. _`Julia Astro on GitHub`: http://github.com/JuliaAstro
.. _`FITSIO.jl`: http://github.com/JuliaAstro/FITSIO.jl
.. _`DustExtinction.jl`: http://github.com/JuliaAstro/DustExtinction.jl
.. _`AstroPy`: http://www.astropy.org
.. _`AstroPy on GitHub`: http://github.com/astropy
.. _`SNCosmo`: http://sncosmo.github.io
.. _`SNCosmo on GitHub`: http://github.com/sncosmo/sncosmo
.. _`paper-tools`: http://github.com/kbarbary/paper-tools
.. _`PhotUtils`: http://photutils.readthedocs.io
.. _`SEP`: http://sep.readthedocs.io
.. _`SEP on GitHub`: http://github.com/kbarbary/sep
.. _`Nestle`: http://kbarbary.github.io/nestle
.. _`Nestle on GitHub`: http://github.com/kbarbary/nestle
.. _`Dierckx.jl`: http://github.com/kbarbary/Dierckx.jl
.. _`TimeIt.jl`: http://github.com/kbarbary/TimeIt.jl
.. _`SkyCoords.jl`: http://github.com/kbarbary/SkyCoords.jl
.. _`Nearby Supernova Factory`: http://snfactory.lbl.gov
.. _`Extinction`: http://extinction.readthedocs.io
.. _`Extinction on GitHub`: http://github.com/kbarbary/extinction
.. _`bsplines`: http://github.com/kbarbary/bsplines
.. _`cubefit`: http://github.com/snfactory/cubefit
