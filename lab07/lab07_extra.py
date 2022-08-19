""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link, value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    rest = link.rest
    previous_link = link
    while rest is not Link.empty:
        if rest.first == value:
            previous_link.rest = rest.rest
        else:
            previous_link = previous_link.rest
        rest = rest.rest

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    change_link = link
    while change_link is not Link.empty:
        if isinstance(change_link.first, Link):
            deep_map_mut(fn, change_link.first)
        else:
            change_link.first = fn(change_link.first)
        change_link = change_link.rest

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    memo = []
    check_link = link
    while check_link is not Link.empty:
        if check_link in memo:
            return True
        memo.append(check_link)
        check_link = check_link.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    def is_cycle_link(in_link):
        check_link = in_link.rest
        while check_link is not Link.empty:
            if check_link == in_link:
                return True
            check_link = check_link.rest
        return False
    check_link = link
    while check_link is not Link.empty:
        if is_cycle_link(check_link):
            return True
        check_link = check_link.rest
    return False

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    even_indexed = True

    def reverse_other_even_indexed(t, even_indexed):
        if even_indexed:
            for index in range(len(t.branches) // 2):
                t.branches[index].label, t.branches[len(t.branches) - index - 1].label = t.branches[len(t.branches) - index - 1].label, t.branches[index].label
        even_indexed = not even_indexed
        for branch in t.branches:
            reverse_other_even_indexed(branch, even_indexed)
    reverse_other_even_indexed(t, even_indexed)
