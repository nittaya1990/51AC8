from skToken import Token, TType


def get_index(string, to_find):
    # Better index (if not found return ending)
    i = 0
    while i < len(string):
        char = string[i]
        if char == to_find:
            break
        i += 1
    return i

def get_end_group(string, group):
    # Given a string find the end of the group
    i = 0
    while i < len(string):
        char = string[1]
        if not (char in group):
            break
        i += 1
    return i

def get_index_token(tokens, char_to_find):
    # Same as get_index but for Token
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.value == char_to_find:
            break
        i += 1
    return i

class Parser:
    def __init__(self, code):
        self.code = code
        self.code_pointer = 0

        self.tokens = []

    def remove_whitespace(self):
        i = 0
        code = ''

        while i < len(self.code):
            char = self.code[i]
            after = self.code[i:] # After the character
            # Check for comments
            if char == '#':
                # Ignore everything until newline
                comment_end = after.index('\n')
                i += comment_end
            elif char == '`':
                # String
                string_end = get_index(after[1:], '`')
                i += string_end + 1
                code += '`'
                code += after[1:string_end]
                code += '`'
            elif char == '\\':
                # Single char skip
                code += '\\' + after[1]
                i += 1
            elif char == ' ' or char == '\n':
                # Skip newlines and spaces
                pass
            else:
                # Otherwise
                code += char

            i += 1

        self.code = code

    def parse(self):
        # Parse code into a list of tokens

        while self.code_pointer < len(self.code):
            char = self.code[self.code_pointer]
            after = self.code[self.code_pointer:]

            if char in "0123456789.":
                number_end = get_end_group(after, "0123456789.e")
                number = self.code[self.code_pointer:self.code_pointer + number_end]
                try:
                    value = int(number)
                except:
                    value = float(number)
                token = Token(value, TType.NUMBER)
                self.tokens.append(token)
                self.code_pointer += number_end - 1
            elif char == '`':
                string_end = get_index(after[1:], '`')
                self.tokens.append(Token('`', TType.COMMAND))
                self.tokens.append(Token(after[1:string_end], TType.STRING))
                self.tokens.append(Token('`', TType.COMMAND))
                self.code_pointer += string_end + 1
            elif char == '\\':
                self.tokens.append(Token('\\', TType.COMMAND))
                self.tokens.append(Token(after[1], TType.STRING))
                self.code_pointer += 1
            else:
                self.tokens.append(Token(char, TType.COMMAND))

            self.code_pointer += 1

        # Implicit output
        if not ('ṭ' in self.code):
            self.tokens.append(Token('ṭ', TType.COMMAND))

        self.match_brackets()

        return self.tokens

    def match_brackets(self):
        i = 0

        while i < len(self.tokens):
            token = self.tokens[i]
            after = self.tokens[i:]
            char = token.value

            if char == '(':
                # While loop
                while_loop_end = get_index_token(after, ')')
                misc = {
                    "start": i,
                    "end": i + while_loop_end
                }
                token.update(misc)
            elif char == ')':
                # End of while loop
                for t in self.tokens:
                    if t.value == '(' and t.misc['end'] == i:
                        misc = {
                            "start": token.misc["start"],
                            "end": i,
                        }

            i += 1

if __name__ == '__main__':
    p = Parser(r"a\ `ab`2e10(i)")
    print("============")
    print(p.code)
    print("============")
    p.remove_whitespace()
    print(p.code)
    print("============")
    print(p.parse())