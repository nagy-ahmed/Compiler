tokens = [("ID", "x"), ("Equal", "=="), ("ID", "55")]


class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0

    def parse(self):
        try:
            self.parse_expression()
            print("Code is syntactically correct.")
        except SyntaxError as e:
            print(f"SyntaxError: {e}")

    # check if current_token match ecpected or not , and increment current_index
    def match(self, expected_type):
        if (
            self.current_index < len(self.tokens)
            and self.tokens[self.current_index][0] == expected_type
        ):
            print(self.tokens[self.current_index][1])
            self.current_index += 1
            return True
        else:
            return False

    # according to place of error this function is work, to show what is the error
    def error(self, expected_type):
        exit(f"Expected {expected_type}, got {self.tokens[self.current_index][0]}")

    # function related to check declaration statements
    def parse_declaration(self):
        # int x = y
        if not self.match("Keyword"):
            self.error("Data Type")
        if not self.match("ID"):
            self.error("ID")
        if (
            not self.match("Assign")
            and not self.match("NotEqu")
            and not self.match("AddAssign")
            and not self.match("SubAssign")
            and not self.match("MulAssign")
        ):
            self.error("Assign")
        if not self.match("ID") and not self.match("Number"):
            self.error("ID or Number")

        # *4-z+5;
        while True:
            if (
                not self.match("Plus")
                and not self.match("Mul")
                and not self.match("Minus")
                and not self.match("Div")
            ):
                self.error("Operator")

            if not self.match("ID") and not self.match("Number"):
                self.error("ID or Number")

            if self.match("Semicolon"):
                break

    # check expression x == > < >= <= y,number
    def parse_expression(self):
        if not self.match("ID"):
            self.error("ID or Number")

        if (
            not self.match("Less")
            and not self.match("Lesser")
            and not self.match("Equal")
            and not self.match("Great")
            and not self.match("Greater")
        ):
            self.error("Operator")

        if not self.match("ID") and not self.match("Number"):
            self.error("ID or Number")


parser = Parser(tokens)
parsed_code = parser.parse()
print(parsed_code)
