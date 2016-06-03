# bktree

A pure-python implementation of BK-trees as described [here](http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees).
Allows for quickly searching for all bit strings within Hamming distance N of some search string.

Inputs must be integers.  The Hamming distance between two strings is calculated as the number of differences
in the unsigned binary representation of that number.

Duplicates are allowed.  That is, if you add the same number twice, you will get that number twice in search results
(think list, not set).

Useful if you have, say, a database of image hashes, and finding duplicate or near-duplicate images.

## Usage

    >>> import bktree
    >>> tree = bktree.Tree([0xff, 0xfe, 0xfd])

    >>> tree.search(0xff, 1)
    [0xff, 0xfe]

## Installation

    pip install bktree

## Future

I may add support for:
- Set-style results (no duplicate values)
- Text strings
- Different comparator functions (e.g. Levenshtein distance)

Pull requests welcome.