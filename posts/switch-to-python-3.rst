.. title: Five reasons to switch to Python 3
.. slug: switch-to-python-3
.. date: 2015-08-23 00:00:00 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I recently took the plunge and switched to using Python 3 on a daily
basis. I found it to be surprisingly straightforward. As a newly
minted Python 3 user, I am now licensed (perhaps even obligated) to
nag Python 2 users about switching. Honestly, for scientific computing
there are `not yet <https://www.python.org/dev/peps/pep-0465/>`_ any
killer features in Python 3 that make a switch tempting. However,
there are still some good reasons for scientific practitioners to
switch. Here are five of them:


1. You will have to eventually.
-------------------------------

Python will be around for a long time. Python 2 will not. You'll
have to switch eventually, so why not do it on your own time, well
before Python 2 `reaches end-of-life support
<http://legacy.python.org/dev/peps/pep-0373/>`_ in 2020?

2. It's not that hard.
----------------------

Most numeric-heavy code (e.g., without much string handling or text
I/O) will require few and straightforward changes.  If you have
comprehensive tests for your code, switching to Python 3 is really just a
matter of running the tests and looking up what needs to be changed
for tests to pass. If you don't have tests, you probably developed
the code by running it and seeing if it worked. In that case, run
it with Python 3 and fix things until it works. If you are
switching permanently, you can use the `2to3
<https://wiki.python.org/moin/2to3>`_ tool to make most changes
automatically. If you need to support both Python 2 and 3
simultaneously, the `six <http://pythonhosted.org/six/>`_ library
has made it relatively painless.

3. At this point it won't get much easier.
------------------------------------------

The majority of widely-used third party packages `support Python 3
<https://python3wos.appspot.com/>`_. In particular, all the major
packages for scientific work (NumPy, SciPy, Matplotlib, etc) have
fully supported Python 3 for some time now. While it depends on
what you use, the likelihood is that all packages you use already
support Python 3. If you find one that doesn't, open an issue (or
add a comment on an existing one) in the issue tracker for the
package.

4. Python 3 will soon become better supported than Python 2.
------------------------------------------------------------

This one is a bit of a prediction. As `more and more developers
switch to using Python 3 on a daily basis
<http://astrofrog.github.io/blog/2015/05/09/2015-survey-results/>`_,
new features in third-party packages will become better "tested"
(through use) on Python 3. This is particularly true of smaller
packages without full test coverage.

5. Be part of the solution.
---------------------------

The Python 2 to 3 transition sort of sucks. The sooner the vast
majority of the community transitions, the sooner we can all stop
spending time stuck awkwardly between two similar but incompatible
languages. Developers can spend less time dealing with the dual
support and more time developing awesome new features.
