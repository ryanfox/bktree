class Node(object):
    def __init__(self, num):
        self.num = num
        self.children = {}

    def __str__(self):
        return self.num


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
            node = Node(num)
            curr = self.root
            distance = self._hamming(num, curr.num)

            while distance in curr.children:
                curr = curr.children[distance]
                distance = self._hamming(num, curr.num)

            curr.children[distance] = node
            node.parent = curr

    def search(self, num, max_distance):
        return self._search(self.root, num, max_distance)

    def _search(self, node, num, max_distance):
        if self._hamming(node.num, num) > max_distance:
            return []

        distance = self._hamming(node.num, num)
        children = [node]
        for child in node.children.values():
            if distance - max_distance <= self._hamming(node.num, child.num) <= distance + max_distance:
                children.extend(self._search(child, num, max_distance))
        return children

    @staticmethod
    def _hamming(num1, num2):
        return bin(num1 ^ num2).count('1')
