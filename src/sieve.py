"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []
    for i in range(len(candidates)+1):
        if len(candidates) != 0:
            p=candidates[0]
        else: break
        candidates=[candidates[i] for i in range(len(candidates)) if candidates[i]%p !=0]
        primes.append(p)
    return primes
