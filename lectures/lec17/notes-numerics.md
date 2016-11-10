#   SCIENTIFIC PROGRAMMING  [13h00]

Last time we focused on the construction of scientific models.  Today we're going to explore some of the implications of scientific modeling on the way we program, as well as how numerical error arises and can be dealt with.

We'll do a quiz later on today.

##  SCIENTIFIC MODELING  [13h01]

"all models are wrong (but some are useful)"

First we talk about 'models', then we talk about 'wrong'.

##  SOURCES OF ERROR  [13h15]

Recollect that I claimed Wednesday that building a model, or rather having a model, says nothing about whether or not the model is correct or whether we should have confidence in its predictions.  Let us posit that we have carefully constructed a model—we've thought through the problem, incorporated the correct physics and mathematics, and made reasonable choices for the implementation and numerics.  Now what can go wrong?

-   our model can oversimplify the real world (of course it almost always does)
    -   Ohm's law example

        ohm’s law is empirical observational relation

        “true” version would hold across all scenarios but breaks down if pressed too far

        (GaAs nonlinear + negative regions, electrochemistry, etc.)

-   our model can lull us into a false sense of adequacy by being right almost all the time (you might say this is a good problem to have)

-   but worst of all are the surprises you don't even anticipate being possible.


##  NUMERICAL ERROR (MACHINE REPRESENTATION)  [13h15]

=>  open jupyter

Suppose you have a lovely little code that has occasion to evaluate statements like this comparison:

    (0.8 - 0.4) == 0.4  # okay
    (1.1 - 0.8) == 0.3  # uh oh

Uh oh. What went wrong?

Another case: repeated summation of a value.

    sum( [ 0.1 ] * 8 )

It even gets worse when associativity and commutativity fail.

    # associativity failure
    (1.0e-8+1.0)-1.0 == 1.0e-8+(1.0-1.0)

    # commutativity failure
    (0.1+0.2+0.3) == (0.3+0.2+0.1)

So what on earth is going wrong and what can you do about it?

It turns out that floating-point numbers, while necessary, are also the handiwork of the Devil.  They'll betray you when you rely too much on them.

Most of the time when we are talking about errors in a code, we mean bugs: systematic unintended errors often arising from our misapprehension of what we wrote (or what we think someone else wrote). However, even in well-written code, errors can arise as a result of how numbers are stored in a computer and how algorithms are carried out. This latter is numerical error.


### FLOATING-POINT REPRESENTATION  [13h20]

We've talked about `float`s as one of the basic number types in Python.  Without delving deeply into their structure, I want you to understand that their representation is finite.

We have not gotten into the way binary numbers work in this class, and we won't beyond this description.

When you create a new `float` variable, somewhere deep in the machine a bunch of bits from memory are allocated and filled.  If you were to encounter this string of bits, what would you make of it?

Well, with floating-point numbers, we define a "binary point" (just like a decimal point).

The values in front of that are powers of two; the values behind it are also powers of two, only fractional.

Summing these values lets us determine the decimal meaning of this number.


### THE LIMITS OF PRECISION  [13h24]

So now we're prepared to return to our earlier example comparing `1.1-0.8` and `0.3` and see what went wrong under the hood.

First compare 0.3 to the result of 1.1−0.8.

    0.3
    1.1-0.8

There's a difference, but why?  Let's look at the binary floating-point representation of 1.1, 0.8, and 0.3 to see.

=> back to slides

Thus you should never compare floating-point values exactly—check to see that they are within a narrow range of each other (with a relative or absolute tolerance, as necessary).

    np.isclose( a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
    np.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)

    np.isclose(1.1-0.8, 0.3)

    np.allclose([1e10,1e-8], [1.00001e10,1e-9])
    np.allclose([1e10,1e-8], [1.0001e10,1e-9])

[Floating-point operations are not true real-valued mathematics: floating-point numbers do not behave exactly like either the real numbers ℝ or the rational numbers ℚ (although integers do behave like a subset of the mathematical integers ℤ).]

More consequences of this:  associativity and commutativity sometimes fail. Indeed, addition is not in general associative for floating-point numbers:

    print( (1.0e-8+1.0)-1.0 )
    print( 1.0e-8+(1.0-1.0) )

Also, truncation in conversion back to integers can be troublesome:

    x = 5.0/9.0
    y = 100*x
    print(y, int(y), round(y))

Now you know something about why your calculations fail in these cases: the finite representation of decimal quantities in binary terms leads to small precision errors that can materially impact comparisons.

Now, I know (because I looked it up) that the largest number representable as a `float` in Python is this:

    import sys
    print(sys.float_info)
    1.7976931348623157e+308

So *logically*, if I add 1 to this number, it should overflow—return infinity.  But it doesn't:

    1.7976931348623157e+308 + 1

What's going on here? It turns out that the relative precision of the added numbers is smaller than the representable precision in the larger number, so there is effectively no addition operation taking place. You have to operate on numbers within each other's field of view, so to speak:

    1.7976931348623157e+308 + 1e300

An elephant can't stand on a flea to get any taller.

### ACCUMULATED ERROR  [13h30]

Imagine a computer system which uses an internal clock giving the time in tenths of a second.  The number is multiplied by the hardware by ten to give the time in seconds.

Now in binary, the representation of 0.1 can be made precise but is an infinitely repeating decimal, like 1/3 in decimal.  So the machine truncates the number for a finite-precision representation.  A very small error is introduced by this, one part in ten million.

However, over one hundred hours, this errors accumulates until the drift error is quite significant.

These numbers describe an event during the Gulf War in 1991.  

A Patriot missile interceptor system used an internal clock which gave the time in tenths of a second. This number was multiplied by 0.1 to give the time in seconds, performed on that machine's hardware. When an Iraqi Scud missile came in, the Patriot system had been on line for about 100 hours. What did this mean in practical terms?

If a Scud missile travels at 1.676km⋅s−1, then in 0.34s it has traveled more than half a kilometer, outside the precision of the interceptor to catch.

This numerical error led, in this case, to the deaths of 28 American soldiers in a barracks in Saudi Arabia.

Now, our precision on modern machines is much higher than the 1980s-era military hardware of the Patriot interceptor.  But clearly I'm not telling you this story for no reason, so let's see what happens

    sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    sum([.1] * 10)

There are error-corrected summation methods which cover cases like this.  One is available in Python from the `math` module as `fsum`:

    from math import fsum
    fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
    fsum([.1] * 10)


##  FINDING & MITIGATING NUMERICAL ERROR  [13h35]

My point is not that you can't trust the machine—merely that you *shouldn't* until you have done some due diligence into its behavior.

In the first place, it is good to use characteristic scales such that most of your expected values lie within the range (10^3 − 10^−3). This allows you to easily identify underflow and overflow errors, as well as gross oscillations and instabilities.

Another way you can detect numerical error is to swap out the 64-bit doubles in your code for 32-bit floats to see what difference, if any, it makes. (Note particularly that in our example the 32-bit float was not susceptible to the error introduced by the vastly more precise double.)

There are better summation tools written specifically for numerics, and if you get into computational science you'll run across those.

Another suggestion is to avoid extreme intermediate values.



##  STYLE  [13h38]

We've laid emphasis on proper documentation in code.  What is included in this?

-   comments on variable meaning and units
-   descriptive variable names
    -   we get away with things like $n$ and $i$ because of mathematical convention

What does this mean?
    seatingAvailable = (guests < 150);
    seatingAvailable = (guests < MaximumOccupancy);

do not use magic numbers!  life lesson territory here, folks

-   hard to change
-   hard to interpret
-   refers to both numbers and string literals

better:

-   use list of defined variables at top
-   use configuration or resource file
