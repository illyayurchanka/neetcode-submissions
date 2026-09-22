class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        arr = []

        for c in tokens:
            match c:
                case '+':
                    val1 = arr.pop()
                    val2 = arr.pop()
                    arr.append(val2 + val1)

                case '-':
                    val1 = arr.pop()
                    val2 = arr.pop()
                    arr.append(val2 - val1)
                case '*':
                    val1 = arr.pop()
                    val2 = arr.pop()
                    arr.append(val2 * val1)
                case '/':
                    val1 = arr.pop()
                    val2 = arr.pop()
                    arr.append(int(float(val2) / val1))
                case _:
                    arr.append(int(c))
        return arr.pop()