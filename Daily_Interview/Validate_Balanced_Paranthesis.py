"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.
"""

# TODO: Complete this
class Validate:
    def __init__(self, item):
        self.item = item

    def validate_item(self):
        # code to validate item
        return True

# Driver code
v = Validate("[()]{}")
v2 = Validate("({[)]")
vv1 = v.validate_item()
vv2 = v2.validate_item()
print(vv1)
print(vv2)
assert vv1 == True
assert vv2 == False