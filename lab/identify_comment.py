class Identifier:
    def __init__(self, text):
        self.text = text
        self.tokens = []

    def is_comment(self):
        items = self.text.split()
        if items[0] == "#":
            return True
        return False


if __name__ == "__main__":
    identifier = Identifier("this is programming")
    print(identifier.is_comment())
