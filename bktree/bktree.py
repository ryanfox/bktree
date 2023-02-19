import sys


if sys.version_info < (3, 10, 0):
    def hamming(num1, num2):
        return bin(num1 ^ num2).count('1')
else:
    def hamming(num1, num2):
        return (num1 ^ num2).bit_count()


class Node(object):
    __slots__ = ('num', 'children', 'parent')

    def __init__(self, num, parent=None):
        self.num = num
        self.children = {}
        self.parent = None

    def __str__(self):
        return str(self.num)


class Tree(object):
    def __init__(self, nums=None):
        self.root = None
        if nums:
            for num in nums:
                self.add(num)

    def add(self, num):
        if self.root is None:
            self.root = Node(num)
        else:
            curr = self.root
            distance = hamming(num, curr.num)

            while distance in curr.children:
                curr = curr.children[distance]
                distance = hamming(num, curr.num)

            curr.children[distance] = Node(num, parent=curr)

    def search(self, num, max_distance):
        candidates = [self.root]
        found = []

        while candidates:
            node = candidates.pop(0)
            distance = hamming(node.num, num)

            if distance <= max_distance:
                found.append(node)

            candidates.extend(child_node for child_dist, child_node in node.children.items()
                              if distance - max_distance <= child_dist <= distance + max_distance)

        return found
