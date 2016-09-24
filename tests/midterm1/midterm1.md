How would the following equation be written as a Python expression?  Assume that `a`, `b` are defined and that `cos` has been `import`ed from `math`.

$$
b
\cos(
a - b
)
^{b}
$$

1.  b cos a-b ** b
2.  b cos(a-b) ** b
3.  b * cos(a-b) ^ b
4.  b * cos(a-b) ** b



What is the result of the following expression?

   [1, 2, 3] * 3

1.  [1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
2.  [1, 2, 3, 1, 2, 3, 1, 2, 3]
3.  [3.0, 6.0, 9.0]
4.  [3, 6, 9]
5.  (3, 6, 9)


The Python keyword `map` applies a function to ​*each item in a `list`*​ and returns the result as a `list`.  For instance, the following would take the square root of each number in a list:

   from math import sqrt
   sqrts = map(sqrt, [ 9.0, 16.0, 2.0, 4.0, 16.0 ] )

and `sqrts == [3.0, 4.0, 1.4142135623730951, 2.0, 4.0]`.

What is the contents of `sums` after this block of code:

   list_of_lists = [ [5, 6, 2], [1, -3, 4], [10, 6, -18] ]
   sums = map( sum, list_of_lists )

a*. [13, 2, -2]
b.  13
c.  [16, 9, -12]
d.  [13]
