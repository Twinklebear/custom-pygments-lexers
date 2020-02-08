# Custom Pygments Lexers

Custom lexers for use with Pygements and minted.

## Minted Usage

Pass minted the Python file and the class name within the file to use. For example,
the OSPRay C Lexer is used as:

```tex
\begin{minted}{c_osp_lexer.py:OSPRayCLexer -x}
// Some code here
\end{minted}
```

