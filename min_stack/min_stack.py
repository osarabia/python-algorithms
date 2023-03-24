

class MinStack:
    """
    MinStack implementation should do push, pop, top, getMin in contant time
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        """
        Append a value to the stack
        """
        if len(self.stack) > 0:
            top_value = self.stack[-1]
            self.stack.append((value, min(value, top_value[1])))
            return
        self.stack.append((value, value))

    def pop(self):
        """
        Remove last element from top of stack
        """
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self):
        """
        retrieve top element from stack
        """
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def get_min(self):
        """
        retrive minimum value element from stack in constant time
        """
        if len(self.stack) > 0:
            return self.stack[-1][1]
        return None
