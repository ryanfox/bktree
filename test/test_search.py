import os
import sys
PARENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PARENT)
import bktree


def test_search():
    descriptor1 = '1011001010011000111101010100010010100110100011000111011110001101'
    descriptor2 = '1011001010011000011101010100010010100110100011100111011110001101'
    descr1 = int(descriptor1, 2)
    descr2 = int(descriptor2, 2)

    tree = bktree.Tree()
    tree.add(descr1)
    assert tree.search(descr2, 1) == []
    assert len(tree.search(descr2, 2)) == 1
    tree.add(descr2)

    # return itself
    result = tree.search(descr1, 1)
    assert len(result) == 1
    assert result[0].num == descr1
    result = tree.search(descr2, 1)
    assert len(result) == 1
    assert result[0].num == descr2

    # return others
    result = tree.search(descr1, 2)
    assert len(result) == 2
    assert result[0].num != result[1].num
    assert result[0].num in (descr1, descr2)
    assert result[1].num in (descr1, descr2)


test_search()
