.. link: 
.. description: 
.. tags: 
.. date: 2014/02/09
.. title: Julia versus NumPy arrays
.. slug: julia-vs-numpy-arrays

`Julia`_ is a new language with a focus on technical computing that
has been getting a lot of `press`_ lately. It promises the ease of use
of a dynamic language like Python while still achieving speeds near
those of a compiled language like C. It does this using `just-in-time
compilation (JIT)`_. In short, Julia's use of JIT allows a programmer
to write functions without type information.  When the function is
called for the first time during program execution, the compiler
inspects the types of the function arguments and compiles a special
version of the function for those specific types, straight to native
machine code. Subsequent calls to the function with the same types use
the already-compiled version of the function.

.. _`Julia`: http://julialang.org
.. _`press`: http://www.wired.com/wiredenterprise/2014/02/julia
.. _`just-in-time compilation (JIT)`:
   http://en.wikipedia.org/wiki/Just-in-time_compilation

Soon after Julia 0.1 was announced in 2012, Wes McKinney posted a
`blog entry <http://wesmckinney.com/blog/?p=475>`_ pointing out that
while Julia's micro-benchmarks are indeed impressive, they
fail to represent what is a common use-case for many technical users:
working with large arrays. He tested a simple example of taking an inner
product of two arrays. Here is a Python/NumPy version:

.. code-block:: python

    from numpy.random import rand
    x = rand(10000000)
    y = rand(10000000)

    (x * y).sum()  # <-- time this

This Python version was significantly faster than an equivalent Julia
version (57.8 ms for Python versus 104.7 ms for Julia). This operation
can be sped up by unwrapping the loop to avoid creating the temporary
array ``x * y`` before summing.  In Julia this can be done efficiently
without the need for compiled extensions and yielded a time of 36
ms. In Python, one needs to compile a C extension using a tool like
Cython. While more arduous, this yielded a time of 14.5 ms, a factor
of nearly 2.5 faster than the best Julia version.

Recently, I started checking out Julia and I wanted to see how this
comparison has changed after the Julia 0.2 release.  I also wanted to
see how the performance comparison depends on the size of the
arrays. My expectation was that with NumPy arrays *the larger the
array, the better the performance*. This is because a larger fraction
of execution time is spent in compiled C loops compared to the
Python wrapper layer.

To aid in running timing tests, I used a ``@timeit`` macro for Julia that
mimics the behavior of the ``%timeit`` magic in IPython. It is in a (very
minimal) `TimeIt.jl`_ Julia package.

.. _`TimeIt.jl`: https://github.com/kbarbary/TimeIt.jl

Array-wise expression (with temporaries)
----------------------------------------

In Python:

.. code-block:: python

    In [2]: from numpy.random import rand

    In [3]: for n in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
       ...:     x = rand(n)
       ...:     y = rand(n)
       ...:     print "n =", n, ":",
       ...:     %timeit (x * y).sum()
       ...: 
    n = 10 : 100000 loops, best of 3: 8.32 µs per loop
    n = 100 : 100000 loops, best of 3: 8.57 µs per loop
    n = 1000 : 100000 loops, best of 3: 11.1 µs per loop
    n = 10000 : 10000 loops, best of 3: 33.2 µs per loop
    n = 100000 : 1000 loops, best of 3: 270 µs per loop
    n = 1000000 : 100 loops, best of 3: 3.5 ms per loop
    n = 10000000 : 10 loops, best of 3: 55.8 ms per loop

In Julia:

.. code-block:: julia

    julia> for n in [10 100 1000 10000 100000 1000000 10000000]
               x = rand(n)
               y = rand(n)
               print("n=$n : ")
               @timeit sum(x .* y)
	   end
    n=10 : 1000000 loops, best of 3: 1.57 µs per loop
    n=100 : 100000 loops, best of 3: 2.13 µs per loop
    n=1000 : 100000 loops, best of 3: 7.80 µs per loop
    n=10000 : 10000 loops, best of 3: 64.60 µs per loop
    n=100000 : 1000 loops, best of 3: 636.59 µs per loop
    n=1000000 : 100 loops, best of 3: 5.97 ms per loop
    n=10000000 : 10 loops, best of 3: 77.88 ms per loop

It seems that things have improved at least somewhat for Julia, as the
time for the largest array is now only a factor of 1.4 slower than
Python. More interesting is the scaling with array size. For small
arrays (up to 1000 elements) Julia is actually *faster* than
Python/NumPy. For intermediate size arrays (100,000 elements), Julia
is nearly 2.5 times *slower* (and in fact, without the ``sum``, Julia
is up to 4 times slower). Finally, at the largest array sizes, Julia
catches up again. (It is unclear to me why; it seems like the
Python/NumPy performance should scale linearly above n=100,000, but it
does not.)

Unwrapped version (no temporaries)
----------------------------------

In Python, to write effecient unwrapped array expressions, we would usually
have to compile a special C extension, typically using a tool like `Cython`_
that automatically takes care of much of the interface between C and Python.
Here is a piece of Cython code to do this:

.. _`Cython`: http://cython.org/

.. code-block:: python

    cimport numpy as np

    def inner(np.ndarray[np.float64_t] x, np.ndarray[np.float64_t] y):
        cdef Py_ssize_t i, n = len(x)
        cdef np.float64_t result = 0.
        for i in range(n):
            result += x[i] * y[i]
        return result

Fortunately, NumPy already includes such a compiled function so we
don't need to bother with the above version:

.. code-block:: python

    In [5]: from numpy import inner

    In [6]: for n in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
       ...:     x = rand(n)
       ...:     y = rand(n)
       ...:     print "n =", n, ":",
       ...:     %timeit np.inner(x, y)
       ...:
    n = 10 : 1000000 loops, best of 3: 791 ns per loop
    n = 100 : 1000000 loops, best of 3: 833 ns per loop
    n = 1000 : 1000000 loops, best of 3: 1.26 µs per loop
    n = 10000 : 100000 loops, best of 3: 6.6 µs per loop
    n = 100000 : 10000 loops, best of 3: 75.9 µs per loop
    n = 1000000 : 1000 loops, best of 3: 1.14 ms per loop
    n = 10000000 : 100 loops, best of 3: 11.4 ms per loop

Here is the corresponding function definition and timings in Julia:

.. code-block:: julia

    julia> function inner(x, y)
               s = 0.
               for i in 1:length(x)
                   s += x[i] + y[i]
	       end
               return s
           end

    julia> for n in [10 100 1000 10000 100000 1000000 10000000]
               x = rand(n)
               y = rand(n)
               print("n=$n : ")
               @timeit inner(x, y)
	   end
    n=10 : 100000000 loops, best of 3: 18.52 ns per loop
    n=100 : 10000000 loops, best of 3: 175.91 ns per loop
    n=1000 : 1000000 loops, best of 3: 1.59 µs per loop
    n=10000 : 100000 loops, best of 3: 15.75 µs per loop
    n=100000 : 10000 loops, best of 3: 158.94 µs per loop
    n=1000000 : 1000 loops, best of 3: 1.73 ms per loop
    n=10000000 : 100 loops, best of 3: 18.75 ms per loop

For someone used to Python and the overheads you get when dealing with
any Python objects, it's pretty incredible to see the near-perfect
linear scaling in Julia all the way down to an array size of 10. For
the smallest array size, Julia is nearly a factor of 50 faster than a
compiled Python C extension.

Conclusions
-----------

Here are the timings relative to the compiled NumPy extension version::

           n  numpy arraywise  julia arraywise  numpy.inner  julia inner
          10           10.518            1.985        1.000        0.023
         100           10.288            2.557        1.000        0.211
        1000            8.810            6.190        1.000        1.262
       10000            5.030            9.788        1.000        2.386
      100000            3.557            8.387        1.000        2.094
     1000000            3.070            5.237        1.000        1.518
    10000000            4.895            6.832        1.000        1.645

The bottom line of Wes McKinney's original post was that for large
array operations, Julia can't beat the performance of NumPy +
Cython. This is still true, although the gap seems slightly smaller in
my tests.

However, I'm still very impressed with Julia. While Cython makes
writing Python C extensions much easier, it still leaves much to be
desired. For any non-trivial task, you need to have a firm
understanding of two separate type systems as well as a knowledge of
how one maps onto the other. In the example Cython ``inner()``
function shown above, it is fairly obvious what is being done, but the
type information would seem opaque to anyone only familiar with Python
or only familiar with C.

In addition to its increased ease, Julia actually gives *better*
performance than Cython for array sizes of less than about 1000
elements. While I sometimes work with large arrays, I often also work
with medium-size or small arrays. In these cases, Cython couldn't match Julia,
unless you're willing to wrap the array operations in more Cython code
at a higher level.
