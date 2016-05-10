.. title: The Joy of Code Refactoring
.. slug: refactoring
.. date: 2016-05-09 00:00:00 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

*Originally published on Feb 29, 2016 here:* https://bids.berkeley.edu/news/joy-code-refactoring

If you write software for your research, you have most likely had the
experience of looking at your code and realizing it has become a
tangled mess. Perhaps it has even gotten to the point where you, the
original author, have a hard time remembering how all the pieces fit
together. Don't despair! This is perfectly natural in research
software; it is just time to *refactor*.


What is refactoring?
--------------------

Code refactoring is the process of restructuring existing computer
code without changing its external behavior in order to make it easier
to understand, reason about, or extend. Much has been written about
refactoring in software engineering and computer science. The term
itself has been in use since at least the early 1990s and the
canonical reference, "Refactoring: improving the design of existing
code" by Martin Fowler was published in 2001. Fowler even maintains a
`catalog <http://www.refactoring.com>`_ of the specific types of code
transformations that are considered refactorings. (Note that though I
use the term "refactoring" in this post, the contents here also apply
to a broader set of code cleaning and restructuring techniques that go
beyond these atomic code transformations.)


Why is refactoring important for researchers?
---------------------------------------------

On the surface, it can seem hard to justify spending time working on
your code only to have it do the exact same thing at the end of the
day. Imagine being a student and explaining to an advisor that you
have produced no new results, but rather have been spending your time
making nebulous "improvements" to your code! However, such code
restructuring is an investment that will make future development
easier. The longer the lifetime of a piece of software and the more
people that need to read and modify it, the more important refactoring
becomes. In fact, I argue that computational scientists *in
particular* should view refactoring as a valuable and even inherent
part of research software development. There are two reasons for this:

(1) **Scientists often don't know what the code they are writing is
    supposed to do before they write it.** For example, when reducing
    or modeling data, there may be peculiarities in the data that only
    become apparent after some analysis. The model or algorithm must
    then be improved to better describe the data or otherwise deal
    with the peculiarities. New requirements often mean that the way
    the code was originally structured is no longer optimal and the
    code should be restructured rather than tacking on new
    functionality to an existing structure that wasn't designed to
    handle it.

(2) **Research software often implements novel algorithms or applies
    existing algorithms to new problems.** Software readability is
    always important, but this aspect of research software makes
    readability paramount: The fine details of an algorithm
    implementation are very often important and, unless you have very
    detailed documentation, the only way to understand exactly what
    the code is doing is by reading it. If you are working in a
    collaboration or publishing your code, maximizing
    understandability will pay dividends in the long term: other
    researchers will be more likely to reuse the code rather than
    throwing up their hands and starting over because they can't
    understand it. Even if your future self is the only one who will
    read the code, it can be a good investment now to spend time
    improving readability, so *you* don't throw up your hands and
    start over.

In research collaborations, the cost of not refactoring is often paid
by those who inherit responsibility for a piece of code. For example,
I and a graduate student took over responsibility of some software
that had been developed in our collaboration over the course of about
three years. The code had grown to about 20,000 lines and included
many unused code paths that had been relevant at some point in
development, but were now only hindering understanding and preventing
us from making necessary improvements. After several months of work
spent understanding the code and refactoring it, were able to reduce
the code base to about 2,200 lines and make it more robust and
extensible in the process. This would have taken far less time overall
if the code had been refactored iteratively during the original
development.


When do you refactor?
---------------------

How do you know when refactoring is needed? Typically, you'll notice a
"code smell" - a surface indication that there is a deeper design
problem. Perhaps you have a single function has grown to be hundreds
of lines long, or perhaps a function has grown to accept tens of
parameters. For me, the inability to quickly recognize what a given
function or class is supposed to do is often a hint that a refactoring
is needed. In the interest of space, I won't go into specifics of
*how* to refactor here, but the references listed below go into great
detail. I will note however that having some sort of automated test(s)
is very helpful for ensuring that the code still works as expected
after refactoring.

In real-world research code, my general approach is to make the
initial design as simple as possible and expect to refactor as I
understand the problem better or as new requirements become
obvious. This is based on an experience that over-designed code (code
that tries to anticipate future requirements or does more than is
required) is particularly detrimental to understandability. Much of my
research code is in Python. In Python, this approach generally means
that I start by mainly writing functions. Later on, it might become
obvious that certain data structures and functions should be grouped
together. Or perhaps I realize that
`polymorphism <https://en.wikipedia.org/wiki/Polymorphism_(computer_science)>`_
would allow me to remove conditional statements spread throughout the
code. At that time, I'll abstract some code into classes. There are
many other aspects to refactoring, but the structure of classes and
functions are the ones I think about most. I've found that this
approach prevents prematurely choosing the `wrong abstraction <http://www.sandimetz.com/blog/2016/1/20/the-wrong-abstraction>`_,
which can be far more costly than refactoring. In the course of
developing a new piece of software, I'll often do several refactorings
that touch large parts of the code.


Summing up
----------

By thinking about refactoring as a natural part of the development
process, you will feel more in control of your code, making future
development more enjoyable. The idea with refactoring is that "you do
not look at your code as some frozen construct that is not susceptible
to change. Instead, you see yourself as capable of maintaining the
code in optimum shape, responding efficiently to new challenges and
changing the code without fear." [4] Who knows, you might even come to
find the refactoring process itself to be enjoyable!


References
----------

1. "Refactoring: improving the design of existing code" by Martin
   Fowler, www.refactoring.com
2. "Refactoring to Patterns" by Joshua Kerievsky
3. "Clean Code: A Handbook of Agile Software Craftsmanship" by Robert
   Cecil Martin
4. http://www.infoq.com/articles/RefactoringMyths
