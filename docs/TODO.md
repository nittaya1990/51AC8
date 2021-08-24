## TODO
Holds what I have remaining.

### TODO:
- [x] Make a TODO.
- [ ] Make a Parser. (The lexer is included)
    - [ ] convert to AST
    - [ ] Match braces `(..){..}`
    - [ ] If statement `{..:..}`
    - [ ] `λ..;` contains code (Its a function)
- [ ] Commands for the interpreter
    - [ ] `λ` Function definition
    - [ ] `@` Function call
    - [ ] `[..]` For each
    - [ ] `(..)` While loop
    - [ ] `{..:..}⁇` If .. else If skip next char
    - [ ] `+-×÷` Addition Subtraction Multiplication Division
    - [ ] `&|~^⌽⊖` Bitwise: And Or Not Xor ShiftLeft(apl's with matrix) ShiftRight(apl with matrix)
    - [ ] `=≠<>≤≥` Comparison 
    - [ ] `%²³½¼¾√∛*` Mod Square Cube .... Power
    - [ ] `Tt` Pop and: Print top as character(s), print top
    - [ ] `©®` Registors, (default: 10)
    - [ ] `¯` Negate, if stack's len is zero push -1
    - [ ] `/₹F` Reduce Map Filter over custom function.
    - [ ] `LrRCBbA` len range Range Complement Binary truthy-falsly Append
    - [ ] `d_≡<backtick>"WU↓↑⇅` Duplicate top 2, Push len, Dup, Swap top 2, Pair top 2, Wrap, Unwrap, Push, pop, reverse
    - [ ] `\` Put next char's value.
    - [ ] `KM` Constants and Math
    - [ ] `Ś⍉I·` Sort Transpose Identity matrix Matmul
    - [ ] `i` Index / Slice
    - [ ] `Ț` push 10
    - [ ] `s` Split into chunks
    - [ ] `#` Reshape (APL/k)
    - [ ] `æ` Is prime?
    - [ ] `→←` Push to / pop from variable
- [ ] Interpreter Flags
    - [ ] `-j` Flag, print the top array seprated by newlines like vyxal.
    - [ ] `-s` Print the stack at the end of the program
    - [ ] `--log` Log file
    - [ ] `-S` Supress output
    - [ ] `-a` Output into an array, that is printed later.
    - [ ] `-N` Reverse the stack after each command