class Symbol:
    def __init__(self, value) -> None:
        self.value = self.parse(value)

    def parse(self, value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
