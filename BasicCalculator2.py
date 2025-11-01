# Time complexity is O(n) and space is also O(n) for using the stack.

# The intuition is to use a stack so as to process the multiplication and division first. And then remaining nums in stack can just be added

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        sign = "+"
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)

            if not c.isdigit() or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    popped = stack.pop()
                    num = num * popped
                    stack.append(num)
                elif sign == "/":
                    popped = stack.pop()
                    stack.append(int(popped / num))
                sign = c
                num = 0

        return sum(stack)

    # Instead of using the stack we can also use calc and keep track of tail so that when we encounter * or / we can remove the tail and do the calculation to apply BODMAS.
    # Here the space will be O(1)
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        calc = 0
        tail = 0
        sign = "+"
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() or i == len(s) - 1:
                if sign == "+":
                    calc += num
                    tail = num
                elif sign == '-':
                    calc -= num
                    tail = -num
                elif sign == '*':
                    calc = (calc - tail) + (tail * num)
                    tail = tail * num
                elif sign == "/":
                    calc = (calc - tail) + int(tail / num)
                    tail = int(tail / num)
                sign = c
                num = 0

        return calc