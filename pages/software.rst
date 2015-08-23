.. link: 
.. description: 
.. tags: 
.. date: 2014/02/08 12:25:03
.. title: Software projects
.. slug: software

All my code is open-source and available on GitHub. This is a list of
the main projects I work on:

====

.. image:: /images/sncosmo.png
   :height: 40px
   :align: left

`SNCosmo`_
----------

SNCosmo is a Python package for supernova cosmology data analysis and
simulation. I'm the creator and main developer. `SNCosmo on GitHub`_.

====

.. image:: /images/astropy.png
   :height: 40px
   :align: left

`AstroPy`_
----------

AstroPy is a community-developed Python library for astronomy.  In the
core package, I designed the layout, style and logo for the
documentation and contributed several functions in the ``stats``
module. I wrote the initial code for the `PhotUtils`_ affiliated
package for photometry and contributed dust extinction laws to the
`SpecUtils`_ affiliated package. `AstroPy on GitHub`_.

====

.. image:: /images/juliaastro.png
   :height: 40px
   :align: left

`JuliaAstro`_
-------------

Astronomy packages for the `Julia`_ programming language.
Lately, I've been working on the `FITSIO.jl`_ package and also
contributed the `DustExtinction.jl`_ package for simple extinction laws.

====

`SEP`_
......

SEP is a Python and C library for source detection and photometry,
adapted from the SourceExtractor code base. I created it in order to
make the SourceExtractor background and detection algorithms available
directly from Python and (eventually) Julia. `SEP on GitHub`_.

====

`Dierckx.jl`_
.............

Dierckx.jl is a package for 1-d and 2-d splines in Julia. It's a
wrapper of the dierckx Fortran library available from NETLIB, the same
library underlying the spline classes in scipy.interpolate.

====

Other
.....

* `Nestle`_  is a fully open-source (MIT-licensed) implementation of nested
  sampling algorithms in Python. It's currently a work in progress.

* `paper-tools`_ contains scripts for preparing papers for
  astronomical journals.

* `TimeIt.jl`_ has a ``@timeit`` macro for Julia, similar to ``%timeit``
  magic in IPython.

.. _`Julia`: http://julialang.org
.. _`JuliaAstro`: http://github.com/JuliaAstro
.. _`FITSIO.jl`: http://github.com/JuliaAstro/FITSIO.jl
.. _`DustExtinction.jl`: http://github.com/JuliaAstro/DustExtinction.jl
.. _`AstroPy`: http://www.astropy.org
.. _`AstroPy on GitHub`: http://github.com/astropy
.. _`SNCosmo`: http://sncosmo.github.io
.. _`SNCosmo on GitHub`: http://github.com/sncosmo/sncosmo
.. _`paper-tools`: http://github.com/kbarbary/paper-tools
.. _`PhotUtils`: http://photutils.readthedocs.org
.. _`SpecUtils`: http://specutils.readthedocs.org
.. _`SEP`: http://sep.readthedocs.org
.. _`SEP on GitHub`: http://github.com/kbarbary/sep
.. _`Nestle`: http://github.com/kbarbary/nestle
.. _`Dierckx.jl`: http://github.com/kbarbary/Dierckx.jl
.. _`TimeIt.jl`: http://github.com/kbarbary/TimeIt.jl
