def generate_token(text):
    result = []
    for char in text:
        if type(char) == str:
            result.append(char)
        else:
            raise SyntaxError(f"Expected string but got {char}")
    return "".join(result).upper()


if __name__ == "__main__":
    res = generate_token("select")
    print(res)

