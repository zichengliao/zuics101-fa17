%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\question{1}
\variant
Consider the following incomplete function.
\begin{verbatim}
def contains_prime(a):
    ???
\end{verbatim}
The function is intended to return \verb|True| if and only if the input list \verb|a| contains at least one prime number and \verb|False| otherwise. Assume a function  \verb|prime| has already been defined which returns \verb|True| if the input integer is prime and \verb|False| otherwise. Which of the following should replace the three question marks to make the function work as described?
\begin{answers}
\answer  \begin{verbatim}for i in range(a):
    if prime(i):
        return False
    return True
\end{verbatim}
\answer \begin{verbatim}for i in a:
    if prime(i):
        return True
    else:
        return False
\end{verbatim}
\answer \begin{verbatim}for i in enumerate(a):
    if prime(i[0]):
        return False
    else:
        return True
\end{verbatim}
\correctanswer \begin{verbatim}for i in zip(a,a):
    if prime(a[0]):
        return True
return False
\end{verbatim}

\end{answers}
\begin{solution}
\end{solution}
