def pascal(row, column):
    """
    https://codereview.stackexchange.com/questions/96211/pascals-triangle-recursion/96213
    >>> pascal(0, 0)
    1
    >>> pascal(5, 4)
    5
    >>> pascal(0, 1)
    0
    """
    if column == 0:
        return 1
    if row == 0:
        return column
    return (row * pascal(row-1, column-1)) / column