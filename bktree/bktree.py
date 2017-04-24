class Node(object):
    def __init__(self, num, user_data=None):
        self.num = num
        self.children = {}
        if user_data is not None:
            self.user_data = user_data

    def __str__(self):
        return str(self.num)


class Tree(object):
    def __init__(self, nums=None):
        self.root = None
        if nums:
            for num in nums:
                self.add(num)

    def add(self, num, user_data=None):
        if self.root is None:
            self.root = Node(num, user_data)
        else:
            node = Node(num, user_data)
            curr = self.root
            distance = self._hamming(num, curr.num)

            while distance in curr.children:
                curr = curr.children[distance]
                distance = self._hamming(num, curr.num)

            curr.children[distance] = node
            node.parent = curr

    def search(self, num, max_distance):
        candidates = [self.root]
        found = []

        while len(candidates) > 0:
            node = candidates.pop(0)
            distance = self._hamming(node.num, num)

            if distance <= max_distance:
                found.append(node)

            candidates.extend(child_node for child_dist, child_node in node.children.items()
                              if distance - max_distance <= child_dist <= distance + max_distance)

        return found

    @staticmethod
    def _hamming(num1, num2):
        return bin(num1 ^ num2).count('1')
