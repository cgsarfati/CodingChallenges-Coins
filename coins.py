"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True


Let's make sure it works when we can spend over 10 pennies::

    >>> coins(11) == {65, 101, 38, 74, 11, 110, 47, 83, 20, 56, 92, 29}
    True

"""

# INSIGHTS
    # num_coins = num_coins + 1 as amount of items in set

    # (1) P, D
    # (2) PP, PD, DD
    # (3) PPP, PPD, PDD, DDD
    # (4) PPPP, PPPD, PPDD, PDDD, DDDD

    # get num_coins, start with P, then switch endings one by one to D until
        # all items in list are D; find recursive way to do this switching
    # output is on a set --> no duplicates, which is helpful.
    # output does math in each combination. need to store penny=1, dime=10


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    # Plan: keep track of coin slots left, path total, & final total
    # Have add_coin fn:
        # to do math, assign penny=1, dime=10
        # with each recursion, decrement coin slots left parameter
        # base case: left == 0 --> stop recursing, add path total to final total
        # progression: 2 recursions (one for +penny, other for +dime)

    # outside add_coin fn, initiate empty set, call add_coin fn, then return result

    def add_coins(left, total, results):
        """Add combos coins to total."""

        # for calculation purposes in total parameter
        dime = 10
        penny = 1

        # BASE: no coin slots left, so add total to results
        if left == 0:
            results.add(total)
            return

        # PROGRESSION: two paths -- one w/ D, other w/ P. Does all P/D combos by end.
        add_coins(left - 1, total + dime, results)
        add_coins(left - 1, total + penny, results)

    # initialize set to be returned
    results = set()

    # start with initial values
    add_coins(left=num_coins, total=0, results=results)

    return results


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
