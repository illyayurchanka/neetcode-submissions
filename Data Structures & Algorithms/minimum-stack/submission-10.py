class MinStack:

    def __init__(self):
        self.array = []
        self.min = [math.inf]

    def push(self, val: int) -> None:
        self.array.append(val)
        if self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        tmp = self.array.pop()
        if tmp == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
