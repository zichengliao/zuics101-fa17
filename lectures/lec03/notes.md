types
strings
indexing

*Promotion* is the phenomenon which occurs when (compatible) data types of different kinds are operated on together.  For instance, a `float` plus an `int` is a `float`.


Of course, some statements are absurd—one must index a string by integers:
    message[8.5]
    => TypeError: string indices must be integers
