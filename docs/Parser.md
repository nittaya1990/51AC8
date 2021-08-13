# Parser
The parser takes tokens generated from the lexer (integrated) and joins
commands.

## How to tokenise
There will be a `consts.py` (or something similar) that will contain constants
like:
```py
# Just examples.
SK_INFIX = "+-/%"
SK_DYAD = "≥≤·"
SK_MONAD = "↑ABCdJEjvm"
```

Then there will be the tokenise function **which shouldn't be in a class**.

The tokenise function works like this:
- Remove comments
- replace braces with `' {brace} '`
- python style `str.split`
- join and split other commands

Then tokenise function will return a list of string. It is the parser's
job to convert it into `Token`
```py
def tokenise(s):
    for c in SK_DYAD:
        s = s.replace(c, f" {c} ")
    ...
```

## The token class
The token class holds 3 things:
- The value of the token
- The `TType` of the token
- Other information as a `dict`.

The first 2 are self-explanatory. The 3rd one however, requires some
explaination.

The `dict` holds:
- Tokens in case of functions.
- Start and end indices in case of brackets.

## The parser class
The parser is a class as to prevent global variables.

The parser loops over the strings (generated from the `tokenise(` function) and
converts them to `Token(` with the appropriate value and holds other information

For example `'12'` will be converted to `Token(12, TType.NUMBER)`
