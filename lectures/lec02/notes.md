expressions
operations
computing

#   `lec02`

### Quiz

A set of instructions executed by a computer to achieve a goal is called:
a.  a process
b.  a program
c.  a procedure
d.  an algorithm

---

A group of eight bits is called:
a.  a nibble
b.  a chomp
c.  a byte
d.  a gobble

---

Python is:
a.  a high-level language
b.  a low-level language

---

Python is:
a.  an interpreted language
b.  a compiled language

---

##  Administration

-   iClicker registration—register your device on the course Compass page

-   You will have a homework assignment due next Wednesday at 5:00 p.m. based on the material from Monday, today, and next Monday.


##  Literals

data that doesn’t change (nouns)
represent a fixed value (`3` or `'firefly'`)

##  Operators

describe how to manipulate data (verbs)
common mathematical operators are examples of this
many other operators exist

##  Expressions

combining literals and operators, we build expressions (sentence fragments, phrases)
expressions are evaluated to produce a new value (3*5, 23-100)
expressions can be very complicated (3+8*5+4-7/100)

order of operations matters!

1+1*2?
a.  4
b.  3
c.  None of the above

---

not always intuitive—when in doubt, use parentheses!

Evaluate this expression:
    23 + 6 / 2 - 4
a.  22
b.  18
c.  -9
d.  None of the above

---

other operators:

-   exponentiation, `**`

-   modulus, `%`  (yes, this weird remainder is very important)
    day of week, for instance

Evaluate this expression:
    (28 % 5) ** 3
a.  8
b.  27
c.  125
d.  None of the above

---

-   floor division, `//`

Bitwise operators:  `|`, `^`, `&`, `<<`, `>>` (don’t need to know)

Evaluate this expression:
    1^2
a.  0
b.  1
c.  2
d.  3

---

(Python exponentiation operator is `**`!)

Computer is in same state as when we started.  Programs are complex, and we need to remember the results *in the machine*—to *store* the resulting value.

The solution:  memory

The new problem:  how do we know where data live?
In low-level languages, data has an address represented in binary

The solution:  give memory locations a name
Variables are a name for a memory location.
Variables store a value.
The value in the variable can change over time—a variable is a place holder.

Assignment operator `=` stores a value in memory
    x = 3
Defines the variable (names it) if we have not already used it

What value is stored in the variable `x`?
x = 17 + 7*9
a.  3
b.  31
c.  55
d.  78

---

What value is stored in the variable `x`?
x = 17 + 7*9
x = 3
a.  3
b.  31
c.  55
d.  78

---

A statement changes the state of the computer (sentence)
An assignment is a statement.
Our programs will consist of series of statements.
A script is a file containing a series of Python statement.
A notebook (as we use in the lab) also collects series of Python statements.
These are stored in text (there’s no magic, just text).
Each instruction is executed in order from top to bottom—together, these statements make up a program.

Example program:
x = 10
y = x**2
y = y + y
