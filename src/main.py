"""
<SQL> ::= <SQL_STMT>
<SQL_STMT> ::= <SELECT_STMT> | <INSERT_STMT> | <UPDATE_STMT>
<SELECT_STMT> ::= "SELECT" <COLUMN> "FROM" <TABLE>
<INSERT_STMT> ::= "INSERT" "INTO" <TABLE> "VALUES" "(" <VALUES> ")"
<UPDATE_STMT> ::= "UPDATE" <TABLE> "SET" <COLUMN> "=" <EXPRESSION> "WHERE" <EXPRESSION>
<COLUMN> ::= "*" | <IDENTIFIER>
<TABLE> ::= <IDENTIFIER>
<VALUES> ::= <IDENTIFIER> "," <VALUES> | <IDENTIFIER>
<EXPRESSION> ::= <IDENTIFIER> <OPERATOR> <LITERAL>
<OPERATOR> ::= "="
<IDENTIFIER> ::= "column1" | "column2" | "table1" | "table2"
<LITERAL> ::= <INTEGER_LITERAL> | <STRING_LITERAL>
<INTEGER_LITERAL> ::= <digit>+
<STRING_LITERAL> ::= '"' <character>* '"'
<digit> ::= "0" | "1" | ... | "9"
<character> ::= any valid character
"""


import logging
import sys
from tokens import generate_token


class SQLParser:
    def __init__(self, sql):
        self.tokens = sql.split()

    def parse(self):
        return self.S()

    def S(self):
        return self.SQL_STMT()

    def SQL_STMT(self):
        token = generate_token(self.tokens[0])
        if token == "SELECT":
            return self.SELECT_STMT()
        elif token == "INSERT":
            return self.INSERT_STMT()
        elif token == "UPDATE":
            return self.UPDATE_STMT()
        return False

    def SELECT_STMT(self):
        if self.tokens[0] == "SELECT":
            self.tokens.pop(0)  # Consume 'SELECT'
            return self.COLUMN() and self.FROM_CLAUSE()
        return False

    def INSERT_STMT(self):
        if self.tokens[0] == "INSERT":
            self.tokens.pop(0)  # Consume 'INSERT'
            return self.INTO_CLAUSE() and self.VALUES_CLAUSE()
        return False

    def UPDATE_STMT(self):
        if self.tokens[0] == "UPDATE":
            self.tokens.pop(0)  # Consume 'UPDATE'
            return self.TABLE() and self.SET_CLAUSE() and self.WHERE_CLAUSE()
        return False

    def COLUMN(self):
        if self.tokens[0] == "*":
            self.tokens.pop(0)  # Consume '*'
            return True
        return self.IDENTIFIER()

    def FROM_CLAUSE(self):
        if self.tokens[0] == "FROM":
            self.tokens.pop(0)  # Consume 'FROM'
            return self.TABLE()
        return False

    def INTO_CLAUSE(self):
        if self.tokens[0] == "INTO":
            self.tokens.pop(0)  # Consume 'INTO'
            return self.TABLE()
        return False

    def VALUES_CLAUSE(self):
        if self.tokens[0] == "VALUES":
            self.tokens.pop(0)  # Consume 'VALUES'
            if "(" in self.tokens and ")" in self.tokens:
                if self.tokens.index(")") > self.tokens.index("("):
                    return True
        return False

    def SET_CLAUSE(self):
        if self.tokens[0] == "SET":
            self.tokens.pop(0)  # Consume 'SET'
            return self.COLUMN() and self.OPERATION() and self.WHERE_CLAUSE()
        return False

    def WHERE_CLAUSE(self):
        if len(self.tokens) < 1:
            logging.error(f"Expected clause or a variable got None")
            return False

        if self.tokens[0] == "WHERE":
            self.tokens.pop(0)  # Consume 'WHERE'
            return self.EXPRESSION()
        return True  # WHERE clause is optional

    def OPERATION(self):
        if self.tokens[0] == "=":
            self.tokens.pop(0)  # Consume '='
            return self.EXPRESSION()

    def EXPRESSION(self):
        if len(self.tokens) < 1:
            logging.error(f"Error near = ")
            return False
        if type(self.tokens[0]) == str:
            return True

        return False



    def TABLE(self):
        return self.IDENTIFIER()

    def IDENTIFIER(self):
        if self.tokens and self.tokens[0] in ["column1", "column2", "table1", "table2"]:
            self.tokens.pop(0)  # Consume the identifier
            return True
        logging.error(f"Table {self.tokens[0]} doesn't exist")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main.py <SQL_statement>")
        sys.exit(1)

    sql_statement = sys.argv[1]
    parser = SQLParser(sql_statement)

    # Parse the SQL statement
    if parser.parse():
        print("SQL statement is valid.")
    else:
        print("SQL statement is not valid.")
