class MinStack:

    def __init__(self):
        self.st = []

    def push(self, value: int) -> None:
        if not self.st:
            self.st.append([value, value])
        else:
            self.st.append([value, min(value, self.st[-1][1])])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]