-   10-min blocks, 5-min activities; concept maps!
-   use beamer + jupyter?

---
#   lec01
#### Objectives
-   Understand course policies and resources.
-   Explain how a computer works schematically.

overview
computing

re hw:  can be a bit more obtuse in phrasing than I prefer, but that's often how things are couched so get used to it

---
#   lec02
#### Objectives
-   Understand hierarchy/rôle of expressions, statements, programs.
-   Combine operators to express mathematical formulae.

#### Quiz
-   What is a program?
-   Details of computer pipeline

expressions
operations
    swap variables (as later piece)
computing
[use parts of old lab2]

---
#   lec03
#### Objectives
-   Apply basic Python types (`int`, `float`, `str`) to adequately store data values.
-   Index elements of a string.

#### Quiz
-   expressions (particularly `^`)
-   operators

types:  int, float, string
strings
indexing
[use parts of old lab2,lab3]

---
#   lec04
#### Objectives
-   Use functions to encapsulate code.
-   Understand how scope masks variable names.
-   Use library functions with `import` to make coding easier.

#### Quiz
-   string indexing
-   types

functions:  what is a $\sin$ function?

scope
import
[start iclicker attendance:  1pt present, 1pt quizzes]

---
#   lec05
#### Objectives
-   Use function parameters to accept data, and function arguments to apply.
-   Name and apply the parts of a function.

#### Quiz
-   What will the following code block output?

        def squinch():
            a = 5
            value = a ** 2

        print( squinch() )

    1.  10
    2.  25
    3.  An empty string:  `''`
    4.  None of the above.


The named parts of a function are:

    def name(parameters):
        """
        docstring
        """
        # comment
        function_body
        return value


arguments
parameters
comments
    docstrings

---
#   lec06
#### Objectives
-   Distinguish between modes of executing code:  notebooks, the interpreter, and scripts.
-   Utilize logical operators (`<`, etc.) to determine truth values.
-   Use the control structure `if` to branch a program's logic.

#### Quiz
-   Label the parts of a function correctly.

        def name(parameters):
            """
            docstring
            """
            # comment
            function_body
            return value

-   being careful with scope, arguments, etc. (values at different points)

scripts
boolean logic
control (if)

---
#   lec07
#### Objectives
-   Create and use lists to store multiple associated data values.
-   Use `list(range(n))` to see how a range is constructed.
-   Iterate over the members of a list using a `for` loop.

#### Quiz
-   boolean logic, control


faded example

loop (for)
range
iteration
list

colors = ['red', 'yellow', 'blue', 'jale', 'ulfire']
for color in colors:
    print(color)

offer to do coffee w/ students?

---
#   lec08
#### Objectives
-   Expand logical branching opportunities with `else` and `elif`, as well as nested `if` statements.
-   Use tuples as a "simpler" (immutable) list.
-   Format strings for data output with format replacement.

#### Quiz
-   `for` loop
-   lists

control (else, elif, nested)
tuples
string formatting
[<= control flow, use some of lab4]

---
#   lec09
#### Objectives
-   Index, sort, and search strings and lists for content; understand the subtleties of their `return` types.

#### Quiz
-   branched control
-   string formatting

indexing
sorting
searching

---
#   lec10
#### Objectives
-   Load file data by the classic `open`, `read`/`readlines`, `close` pipeline.
-   Access data inside of nested lists using multidimensional indexing.

#### Quiz
-   indexing, sorting, searching

file I/O:  open/read/close
nested lists
multidimensional indexing

---
#   lec11
#### Objectives
-   Store and access data in `dict`s.

#### Quiz
-   file I/O process
-   multidimensional indexing

dicts

---
#   mt1

---
#   lec12
#### Objectives
-   Access web-based data sources using `requests`.
-   Review functions and understand default values.
-   Use named tuples to collect associated data values.

#### Quiz
-   `dict`s

requests (webdata)
kwargs + defaults
named tuples
etc.

---
