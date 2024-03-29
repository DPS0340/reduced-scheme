class Symbol:
    def __init__(self, value) -> None:
        self.value = self.parse(value)

    def parse(self, value):
        # from https://norvig.com/lispy.html
        try:
            return float(value)
        except ValueError:
            return value
