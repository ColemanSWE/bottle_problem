from Bottle_Problem import comparison
from Bottle_Problem import big_to_small
from Bottle_Problem import InvalidTargetError
from Bottle_Problem import InvalidGcdRatioError


"""
Testing the exceptions first

InvalidTargetError works
print(big_to_small(11, 7, 5))

InvalidGCDRatioError works
big_to_small(3, 8, 6)
"""

assert comparison(4, 5, 3) == comparison(4, 5, 3) == 6

assert comparison(1, 5, 3) == 4




