#   CS 101 Final Exam

##  Python Multiple-Choice Questions

The following eighteen questions concern Python.

test understanding of shallow/deep copy
1.  Consider the following unit test.
        
        assert permute(1,2,3,4,5) == 2,3,4,5,1
        
    Which of the following programs successfully passes this test?  (Assume that any necessary modules have been imported.)
        
    1.  ```
        def permute(a,b,c,d,e):
            return itertools.permutations(a,b,c,d,e)
        ```
    2.  ```
        def permute(b,c,d,e,a):
            return itertools.permutations( (a,b,c,d,e), 5 )
        ```
    3.  ```
        def permute(a,b,c,d,e):
            return e,a,b,c,d
        ```
    4.  ```*
        def permute(e,a,b,c,d):
            return a,b,c,d,e
        ```

test understanding of list behavior PM1.15
2.  Consider the following Python program.
        
        x = ['snip', 'snap', 5]
        x[0] = x.sort()
        x = x[-2]
        
    What is the type of the final value of `x`?
    
    1.  `list`
    2.  `str`*
    3.  `int`
    4.  `NoneType`

named args/defaults
3.  *For this problem, you should compose a function which accomplishes a given task using the available code blocks arranged in the correct functional order.  (Ignore indentation for this problem.)*
    
    `is_close` should accept two numbers `a`, `b` and (optionally) a relative tolerance `rtol`.  `is_close` should `return` `True` or `False` depending on whether or not the numbers are closer than `rtol`:
    
    $$
    \frac{|a-b|}{b} \leq \texttt{rtol} \rightarrow \texttt{True}
    \frac{|a-b|}{b} >  \texttt{rtol} \rightarrow \texttt{False}
    $$
    
    If `rtol` is not specified, then the default value should be `1e-3`.  The code should return `None` if the calculation fails (for instance, if the parameters `a` or `b` are non-numeric).
        
        def is_close( a, b, rtol=1e-3 ):
            try:
                return ( abs(a-b)/abs(b) <= rtol )
            except:
                return None
        
    1.  `except:`
    2.  `def is_close( a, b, rtol=1e-3 ):`
    3.  `try:`
    4.  `return None`
    5.  `def is_close( a, b, rtol ):`
    6.  `rtol = 1e-3`
    7.  `return ( abs(a-b)/abs(b) <= rtol )`
    8.  `return ( (a-b)/b <= rtol )`
    
    1.  2, 3, 7, 1, 4*
    2.  2, 3, 8, 1, 4
    3.  2, 7
    4.  5, 6, 3, 7, 1, 4
    5.  5, 6, 7
    
    Consider the following incomplete Python program.
        
        def is_close( <missing> ):
            return 
        
        x = np.linspace( 0, 4*np.pi, 101 )
        y1 = np.cos( x )
        y2 = np.sin( x )
        
        <missing>
        plt.show()
        
    
        
    1.  `plt.plot( x, y1, y2, 'b-', 'r-' )`
    2.  `plt.plot( x, y1, 'b-', x, y2, 'r-' )`
    3.  `plt.plot( y1, y2, x, ['b-', 'r-'] )`
    4.  `plt.plot( x, y1, x, y2, ['b-', 'r-'] )`


test syntax
4.  Consider the following Python program.
        
        a = list('zugzwang')
        a.reverse()
        a[1], a[2] = a[2], a[3]
        x = ''
        for e in a:
            x += e
    
    What is the final value of `x`?
    
    1.  `'gawwzguz'`*
    2.  `''`
    3.  `''`
    4.  `''`

distinguish fruitful functions & sorting
5.  Consider the following Python program.
        
        chars = ['arthur', 'mordred', 'morgana', 'lot']
        kings = [chars[3], chars[0]]
        chars[3] = 'pellinore'
        kings = kings.sort()
    
    What is the final value of `kings`?
    
    1.  `['arthur', 'pellinore']`
    2.  `['arthur', 'lot']`
    3.  `None`*
    4.  The program fails to complete.

test key/dict issues
6.  Which of the following Python programs completes without an error?  Assume the following dictionary is available.
        
        mydict = { 'a':1, 'b':2, 'c':3 }
        
    1.  SyntaxError (missing :)
        ```
        for key in mydict.keys()
            mydict[key] = key.upper()
        mydict['D'] = 4
        ```
    2.  KeyError
        ```
        for value in mydict.values():
            mydict[value] = value.upper()
        mydict['D'] = 4
        ```
    3.  TypeError
        ```
        for key in mydict.keys():
            mydict[key] = mydict[key].upper()
        mydict.append('D':4)
        ```
    4.  correct
        ```
        for key in mydict.keys():
            mydict[key] = key.upper()
        mydict['D'] = 4
        ```

try/except
7.  Consider the following Python program.
        
        a = [7.0, '5', '3', 1]
        x = ''
        for e in a:
            try:
                x += e
            except:
                x += 'A'
        
    What is the final value of `x`?
    
    1.  `'7.0AA0'`
    2.  `'7AA0'`
    3.  `'A53A'`*
    4.  None of the other answers are correct.

matplotlib
8.  Consider the following incomplete Python program.
        
        import numpy as np
        import matplotlib.pyplot as plt
        
        x = np.linspace( 0, 4*np.pi, 101 )
        y1 = np.cos( x )
        y2 = np.sin( x )
        
        <missing>
        plt.show()
        
    The program should plot the `y1` data as a blue line and the `y2` data as a red line, both against `x`.  What should replace the `<missing>` block to complete the program?
        
    1.  `plt.plot( x, y1, y2, 'b-', 'r-' )`
    2.  `plt.plot( x, y1, 'b-', x, y2, 'r-' )`
    3.  `plt.plot( y1, y2, x, ['b-', 'r-'] )`
    4.  `plt.plot( x, y1, x, y2, ['b-', 'r-'] )`

test np indexing
9.  Consider the following two-dimensional NumPy array, stored in the variable `A`.
    
    $$
    \begin{bmatrix}
      1 &    2 &    4 \\
      8 &   16 &   32 \\
     64 &  128 &  256 \\
    512 & 1024 & 2048
    \end{bmatrix}
    $$
    
    How can we index and retrieve the value 16?
    
    1.  `A[1,2]`*
    2.  `A[2,3]`
    3.  `A[3,2]`
    4.  `A[2,1]`

test np indexing
10. Consider the following Python program.
        
        import numpy as np
        x = np.zeros( (3,3) )
        for i in range(3):
            for j in range(3):
                x[i,j] = i*j + i
        
    What is the final value of `x`?
    
    1.  correct
    2.  flip i/j
    3.  range 1–3 instead of 0–2
    4.  No other answer is correct.

test np indexing
11. Consider the following Python program.
        
        import numpy as np
        x = np.ones( (3,3) )
        for i in range(3):
            for j in range(i):
                x[i,j] = i*j + j
        
    What is the final value of `x`?
    
    1.  correct
    2.  flip i/j
    3.  range to value (instead of one less)
    4.  No other answer is correct.

recognizing efficiencies
12. You are required to calculate X as efficiently as possible.  Which of the following candidate programs will correctly complete fastest?
    
    1.  C&D
    2.  brute force
    3.  opt but calling instead of storing results in vars
    4.  opt*

test numerical error understanding
13. Which of the following comparisons carries a high risk of numerical error?  (In other words, which of these is susceptible to unexpected behavior?)  Assume that all variables are numeric and defined, and that any necessary modules have been imported.
    
    1.  `round(a + b) == 4`
    2.  `a + b == 0.3`*
    3.  `abs(a + b)/c <= 1e-3`
    4.  `isclose(a, b)`

test ability to follow algorithmic logic
14. Consider the following Python program.
        
        d = {}
        for i,c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            d[c] = i
        x = 0
        for c in 'somestring':
            x += d[c]
        
    What is the final value of `x`?
    
    1.  
    2.  
    3.  
    4.  

test ability to follow algorithmic logic
15. Consider the following incomplete Python program.
        
        sum = 0
        i = 1
        for i in range(1000):
            <missing>
        print(sum)
        
    The program should sum all perfect squares from 1 to 100 (inclusive).  What should replace the `<missing>` block to complete the program?
    
    1.  `sum = i*i`
    2.  `sum + i*i`
    3.  `sum += i*i`*
    4.  `sum == sum + i^2`

test code construction ability
16. *For this problem, you should compose a function which accomplishes a given task using the available code blocks arranged in the correct functional order.  (Ignore indentation for this problem.)*
    
    `find_min` should accept a `list` and `return` the value of the minimum item in the `list`.  We initialize the list with `float('Inf')` as the highest representable value, guaranteeing that all members of the list are lower than the initial value.  Assume that all members of `my_list` are numeric.
        
        def find_min(my_list):
        
    1.  `min_val = i`
    2.  `min_val = float('Inf')`
    3.  `for i in range(len(my_list)):`
    4.  `if i > min_val:`
    5.  `min_val = my_list[i]`
    6.  `return min_val`
    7.  `for i in range(my_list):`
    8.  `if my_list[i] < min_val:`
    9.  `print(min_val)`
    
    1.  2, 3, 4, 1, 6
    2.  3, 1, 8, 5, 9
    3.  2, 3, 8, 5, 6*
    4.  2, 7, 4, 5, 6
    5.  2, 3, 8, 1, 6

test random number generation
17. Which of the following lines of Python code best simulates the roll of one die?
    
    1.  `x = np.random.choice( np.arange(1,7) )`*
    2.  `x = np.random.shuffle( np.arange(1,7) )`
    3.  `x = np.random.randn( np.arange(1,7) )`
    4.  `x = np.random.rand( np.arange(1,7) )`

numerical ability
18. Consider the following incomplete Python program.
        
        def fib(n):
            if n <= 1:
                return 1
            else:
                <missing>
        
    The function `fib` should return a list of the Fibonacci sequence, where each number is equal to the sum of the two preceding numbers; *i.e.*,
    
    $$
    1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    $$
    
    What should replace the `<missing>` block to complete the program?
    
    1.  `return fib(n-1) + fib(n-2)`*
    2.  `return fib(n) + fib(n-1)`
    3.  `return fib(n-1, n-2)`
    4.  `return (n-1) + (n-2)`


##  MATLAB Multiple-Choice Questions

The following ten questions concern MATLAB.

test indexing PF1
19. Consider the following MATLAB program.
        
        A = ones(3,3) - eye(3,3);
        A *= 2;
        A(1:2, :) += 3; 
        
    What is the final value of `A`?

test range PF3
20. Consider the following MATLAB program.
        
        x = 1:3;
        y = 2:4;
        z = [x; y];
        
    What is the final value of `z`?

test loops PF15
21. Consider the following MATLAB program.
        
        A = eye(3,3);
        for x=1:2:3
            for y=1:3
                A(x,y) = A(y,x)+1;
            end
        end
        
    What is the final value of `A`?
    
    1.  wrong w/ flipped x/y
    2.  right
    3.  wrong w/o updating A
    4.  wrong w/ x=1:3

test syntax + logic
22. Consider the following MATLAB program.
        
        x = 2*eye( 2,2 );
        y = [  1  2; 3 4 ];
        z = [ y' x'; x y ];
        
    What is the final value of `z`?
    
    1.  $$*
        \begin{bmatrix}
        1 & 3 & 2 & 0 \\
        2 & 4 & 0 & 2 \\
        2 & 0 & 1 & 2 \\
        0 & 2 & 3 & 4
        \end{bmatrix}
        $$
    2.  $$
        \begin{bmatrix}
        1 & 2 & 2 & 0 \\
        3 & 4 & 0 & 2 \\
        2 & 0 & 1 & 3 \\
        0 & 2 & 2 & 4
        \end{bmatrix}
        $$
    3.  $$
        \begin{bmatrix}
        4 & 3 & 0 & 2 \\
        2 & 1 & 2 & 0 \\
        2 & 0 & 1 & 3 \\
        0 & 2 & 2 & 4
        \end{bmatrix}
        $$
    4.  $$
        \begin{bmatrix}
        1 & 3 & 2 & 2 \\
        2 & 4 & 2 & 2 \\
        2 & 2 & 1 & 2 \\
        2 & 2 & 3 & 4
        \end{bmatrix}
        $$

test polynomial operations
23. Recollect that MATLAB represents polynomials as an array from the highest-order coefficient to the lowest.  For instance,
    
    $$
    f(x) =
    \left(
    3 x^{2} + 2 x + 1
    \right)
    $$
    
    is written as the MATLAB array
        
        [3 2 1]
        
    How would we represent the summation of these two polynomials, $g(x) + h(x)$?
    
    $$
    g(x) =
    \left(
    - x^{2} + 3 x + 1
    \right)
    $$
    $$
    h(x) =
    \left(
    2 x^{3} + 4 x + 1
    \right)
    $$
    
    1.  [-1 3 1] + [2 4 1]
    2.  [-1 3 1] + [2 0 4 1]
    3.  [0 -1 3 1] + [2 0 4 1]*
    4.  [-1 3 1 0] + [2 0 4 1]
    5.  [1 3 -1] + [1 4 2]

test syntax
24. Consider the following two-dimensional MATLAB array, stored in the variable `A`.
    
    $$
    \begin{bmatrix}
      1 &    2 &    4 \\
      8 &   16 &   32 \\
     64 &  128 &  256 \\
    512 & 1024 & 2048
    \end{bmatrix}
    $$
    
    How can we index and retrieve the value 128?
    
    1.  `A(1,2)`
    2.  `A(2,3)`
    3.  `A(3,2)`*
    4.  `A(2,1)`

test syntax
25. Consider the following function.
        
        function [a b] = squrge(x, y)
            a = x ^ 2;
            b = a * 3 + y;
        end
        
    Which of the following correctly assigns the result of `a` to `A` and `b` to `B`?
    
    1.  [A B] = squrge(5, 4);*
    2.  [A B] = squrge[5 4];
    3.  A,B = squrge(5, 4);
    4.  [A B] = squrge([5 4]);

test ability to follow algorithm logic
26. Consider the Taylor series definition of the sine function:
    
    $$
    \sin (x) =
    x
    - \frac{x^3}{3!}
    + \frac{x^5}{5!}
    - \frac{x^7}{7!}
    ...
    $$
    
    The series converges for all real $x$, so to calculate $\sin(x)$ to within a few decimal places of accuracy one just needs to include enough terms in the calculation.  (Recall that factorial is defined as $n! = n \times (n-1) \times ... \times 2 \times 1$; thus $1! = 1$, $3! = 6$, etc.)
    
    Which of the following candidate programs successfully calculates the value of $sin(x)$ for all $x$ to three decimal places of accuracy?
    
    1.  ```*
        function [ y ] = my_sin( x )
            y = 0;
            yold = 1;
            n = 0;
            atol = 1e-3;  % tolerance
            while (abs(y-yold) > atol)
                yold = y;
                term = (x ^ (2*n+1)) / factorial((2*n+1))
                if (mod(n,2) == 1)
                    term = -term;
                end
                y = y + term;
                n = n + 1;
            end
        end
        ```
    2. wrong because set arbitrary cap on for
        ```*
        function [ y ] = my_sin( x )
            y = 0;
            yold = 1;
            atol = 1e-3;  % tolerance
            for n=0:10
                yold = y;
                term = (x ^ (2*n+1)) / factorial((2*n+1))
                if (mod(n,2) == 1)
                    term = -term;
                end
                y = y + term;
                if (abs(y-yold) <= atol)
                    break
                end
            end
        end
        ```
    3. wrong because forget to set $n$ properly
        ```
        function [ y ] = my_sin( x )
            y = 0;
            yold = 1;
            n = 1;
            atol = 1e-3;  % tolerance
            while (abs(y-yold) > atol)
                yold = y;
                term = (x ^ n) / factorial(n)
                if (mod(n,2) == 1)
                    term = -term;
                end
                y = y + term;
                n = n + 1;
            end
        end
        ```
    4. wrong because don't break at correct time
        ```
        function [ y ] = my_sin( x )
            y = 0;
            yold = 1;
            n = 1;
            atol = 1e-3;  % tolerance
            while (y-yold > atol)
                yold = y;
                term = (x ^ n) / factorial(n)
                if (mod(n,2) == 1)
                    term = -term;
                end
                y = y + term;
                n = n + 1;
            end
        end
        ```

test code construction ability
27. *For this problem, you should compose a function which accomplishes a given task using the available code blocks arranged in the correct functional order.*
    
    `cross_prod` should accept two column vectors `a` and `b` and `return` the value of the cross product,
    $$
    \vec{c} =
    \vec{a} \times \vec{b} =
    \begin{bmatrix}
        a_2 b_3 - a_3 b_2
        a_3 b_1 - a_1 b_3
        a_1 b_2 - a_2 b_1
    \end{bmatrix}
    $$
    
    function [ c ] = cross_prod( a,b )
        c = zeros( 3,1 );
        c(1) = a(2)*b(3) - a(3)*b(2);
        c(2) = a(3)*b(1) - a(1)*b(3);
        c(3) = a(1)*b(2) - a(2)*b(1);
    end
    
    1.  `end`
    2.  `c(1) = a(2)*b(3) - a(3)*b(2);`
    3.  `function [ c ] = cross_prod( a,b )`
    4.  `c(2) = a(3)*b(1) - a(1)*b(3);`
    5.  `c = zeros( 3,1 );`
    6.  `c(3) = a(1)*b(2) - a(2)*b(1);`
    7.  `c = zeros( 1,3 );`
    8.  `c = a .* b - b .* a;`
    9.  `cross_prod = function( a,b )`
    
    1.  3, 5, 2, 4, 6, 1*
    2.  3, 7, 2, 4, 6, 1
    3.  9, 5, 8, 1
    4.  9, 7, 2, 4, 6, 1
    5.  3, 7, 8, 1

test logic
28. Consider the following MATLAB program.
        
        s = (3 < 5) || ((2 > 3) && (1 ~= 0))
        
    What is the final value of `s`?
    
    1.  `1`*
    2.  `True`
    3.  `False`
    4.  `0`


##  Python Coding Questions

The following two questions concern Python.

29. Compose a Python script which prints out each number from 1 to 100.  For each number, the following set of rules should be applied to the output:
    
    1.  If the number is divisible by three, print the number followed by "fizz".
    2.  If the number is divisible by five, print the number followed by "buzz".
    3.  If the number is divisible by both three and five, print the number followed by both "fizz" and "buzz".
    4.  Otherwise, just print the number.
    
    For instance, the expected output from 9 to 16 will be:
        
        9fizz
        10buzz
        11 
        12fizz
        13
        14
        15fizzbuzz
        16

30. We want to design the best spacecraft for a long-term mission.  We will explore three design variables:  material of construction; means of propulsion; and fuel source.  There are thousands of possible materials, dozens of means of propulsion, and hundreds of possible energy sources (assuming that means of propulsion and energy source are decoupled).  Assume we have these possibilities stored as strings in three lists named `materials`, `propulsions`, and `fuels`.  Also, assume we have a function available called `economize` which takes three string arguments (the names of a particular material, propulsion means, and energy source) and returns a floating point number indicating how expensive that particular combination of design variables is (a lower result indicates a more economical means of long-term space travel).
    
    Compose a Python script to brute force search for the solution of the cheapest means of space flight in this scenario.  You may not use `import`.  Store the resulting combination of design variables as a tuple named `starship`.