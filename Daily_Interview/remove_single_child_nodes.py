"""
Given a binary tree, remove all `nodes which contain only a single child
Eg.
      1                 1
     / \\               / \\
    2   3     ->      0   3
   /   / \\               / \\
  0   9   4             9   4


"""


class Node:
    def __init__(self, value: int, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def check_and_remove(current: Node):
    if current is None or current.left is None and current.right is None:
        return  # break condition here, leaf node
    
    if current.left != current.right and current.left is None or current.right is None:  # Xor logic
        print("Removing for node: {}".format(current.value))
        if current.left:
            # connect left to parent
            current.left.parent = current.parent
            if current.parent.left == current:
                current.parent.left = current.left
            else:
                current.parent.right = current.left
        else:
            # connect right to parent
            current.right.parent = current.parent
            if current.parent.left == current:
                current.parent.left = current.right
            else:
                current.parent.right = current.right

    # traverse down children
    check_and_remove(current.left)
    check_and_remove(current.right)


def removal_implementation(root: Node) -> None:
    """
    Main implementation here
    Mutates binary tree
    """
    # recursively check left and right
    check_and_remove(root)


def run_driver():
    # Simple test case as above

    # build binary
    root = Node(1)

    l2_1 = Node(2, parent=root)
    l2_2 = Node(3, parent=root)
    root.left, root.right = l2_1, l2_2

    l3_1 = Node(0, parent=l2_1)
    l3_2 = Node(9, parent=l2_2)
    l3_3 = Node(4, parent=l2_2)
    l2_1.left = l3_1
    l2_2.left, l2_2.right = l3_2, l3_3

    removal_implementation(root)
    root.display()


run_driver()


