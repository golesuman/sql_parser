import re


def generate_token(text):
    result = []
    for char in text:
        if re.match("^[a-zA-Z]$", char):
            result.append(char)
        else:
            raise SyntaxError(f"Expected string but got '{char}'")
    return "".join(result).upper()


if __name__ == "__main__":
    res = generate_token("1elect")
    print(res)
