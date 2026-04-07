"""Simple stack implementation usin list.
two methods: push and pop.
"""

class Stack:
    """Stack object with push and pop methods."""
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Add item to the top of the stack."""
        self._items.append(item)
    
    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def __len__(self):
        """Return the number of items in the stack."""
        return len(self._items)
    
    def __repr__(self):
        """Return a string representation of the stack."""
        return f"<{type(self).__name__})> at {id(self):#x}> size={len(self)}"
    

class NumbericStask(Stack):
    """Stack that only accepts numeric values."""
    def push(self, item):
        """Add item to the top of the stack if it's numeric."""
        if not isinstance(item, (int, float)):
            raise TypeError("Only numeric values are allowed")
        super().push(item)

if __name__ == "__main__":
    a_stack = Stack()
    a_stack.push(1)
    a_stack.push(2)
    a_stack.push(3)
    print(repr(a_stack))
    print(a_stack)  # Stack(Stack)
    print(len(a_stack))  # 3
    print(a_stack.pop())  # 3
    print(a_stack.pop())  # 2
    print(a_stack.pop())  # 1
    try:
        a_stack.pop()  # This will raise an error
    except IndexError as e:
        print(e)  # pop from empty stack
    num_stack = NumbericStask()
    num_stack.push(1)
    num_stack.push(2.5)
    print(repr(num_stack._items))
    print(num_stack)
    try:
        num_stack.push("string")  # This will raise an error
    except TypeError as e:
        print(e)  # Only numeric values are allowed
