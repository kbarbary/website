.. title: Cython and multiple NumPy dtypes
.. slug: cython-and-multiple-numpy-dtypes
.. date: 2014-10-26 12:00:00 UTC
.. tags: 
.. link: 
.. description: 
.. type: text

Earlier this summer, I was attempting to use Cython to wrap a C library that
deals with arrays. There's a excellent `tutorial`_ on the Cython wiki
on this topic. In the example given there, the Python function can
only accept arrays of a single datatype: C double (or equivalently,
``numpy.float64``). The cython function signature

.. code-block:: cython

   def multiply(np.ndarray[double, ndim=2, mode="c"] input not None, double value):

means that an error will be raised if the input array has any numpy
dtype other than float64. But, why should the ``multiply`` function
operate only on arrays of doubles? Python users are used to having a
single function transparently operate on numpy arrays of many
different dtypes. Let's make the single ``multiply`` function work on
both float and double arrays!

This supposes that you have multiple C functions for
different array types. We want our Python function to check the
datatype of the input array (at runtime) and then *dispatch* to the
appropriate C function for that data type (or raise an Exception of
the datatype is not supported).

I eventually found a post in a `thread on cython-users`_ that
describes how to do this, and the following is based on that answer.

First, suppose we have two separate implementations of the C function for
different data types:

.. code-block:: c

   /*
   c_multiply.c

   simple C functions that alters data passed in via a pointer

   */

   void c_multiply_dbl(double* array, double multiplier, int m, int n) {
       int i;
       for (i = 0; i < m*n; i++)
         array[i] = array[i] * multiplier;
       return;
   }

   void c_multiply_flt(float* array, double multiplier, int m, int n) {
       int i;
       for (i = 0; i < m*n; i++)
         array[i] = array[i] * multiplier;
       return;
   }

The Cython code will be as follows:

.. code-block:: cython

   import numpy as np
   cimport numpy as np

   cdef extern:
       void c_multiply_dbl(double* array, double multiplier, int m, int n)
       void c_multiply_flt(float* array, double multiplier, int m, int n)

   def multiply(np.ndarray input not None, double value):
        cdef int m, n

        # declare a numpy array of raw bytes (unsigned 8-bit integers)
        # and assign it to a view of the input data.
	cdef np.uint8_t[:, :] buffer
	buffer = input.view(np.uint8)

	# get shape
	m, n = input.shape[0], input.shape[1]

	# choose the appropriate routine based 
	if input.dtype == np.float64:
	    c_multiply_dbl(<double *>&buffer[0, 0], value, m, n)
	elif input.dtype == np.float32:
	    c_multiply_flt(<float *>&buffer[0, 0], value, m, n)
	else:
	    raise ValueError("dtype {0} not supported".format(input.dtype))


The key line is ``buffer = input.view(np.uint8)`` where buffer is
declared at compile time as a 2-d numpy array of raw bytes. Having
this compile-time type allows us to later perform the operation
``&buffer[0, 0]`` in order to get the address of the underlying data
buffer in the array. We would not have been allowed to perform this
operation directly on the input array. Note that
``input.view(np.uint8)`` does not copy the data in ``input`` so this
is a relatively cheap operation.

The code can then be built with the following ``setup.py`` file:

.. code-block:: python

   #!/usr/bin/env python

   from distutils.core import setup
   from distutils.extension import Extension
   from Cython.Distutils import build_ext

   import numpy

   setup(
       cmdclass = {'build_ext': build_ext},
       ext_modules = [Extension("multiply",
                                sources=["multiply.pyx", "c_multiply.c"],
				include_dirs=[numpy.get_include()])],
       )

and by then running ``python setup.py build_ext --inplace``. This creates
a Python module ``multiply.so`` that you can import in a Python session.
We can verify that it works on 2-d arrays of both 32-bit and 64-bit floats!

.. code-block:: python

   >>> import numpy as np
   >>> import multiply
   >>> x = np.ones((2, 2), dtype=np.float32)
   >>> multiply.multiply(x, 2)
   >>> x
   array([[ 2.,  2.],
          [ 2.,  2.]], dtype=float32)
   >>> y = np.ones((2, 2), dtype=np.float64)
   >>> multiply.multiply(y, 2)
   >>> y
   array([[ 2.,  2.],
         [ 2.,  2.]])

.. _`tutorial` : https://github.com/cython/cython/wiki/tutorials-NumpyPointerToC
.. _`thread on cython-users`: https://groups.google.com/d/msg/cython-users/VW_AH2HEFfU/vmrl_QntubsJ
