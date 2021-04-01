from math import sqrt
from typing import Any
from typing import Generator
from typing import Optional


def primes(n: Optional[int], priority: str = "speed") -> Generator[int, None, None]:
    """
    Prime numbers generator up to N
    :param n: Limit of prime numbers generator (if None then infinite loop)
    :param priority: Algorithm efficiency type ("speed" or "memory")
    :return: Generator of prime numbers
    """
    __is_positive_integer(n)
    if priority == "speed":
        return __primes_with_speed_priority(n)
    elif priority == "memory":
        return __primes_with_memory_priority(n)
    else:
        pass


def __primes_with_speed_priority(n: Optional[int]) -> Generator[int, None, None]:
    """
    Prime numbers generator up to N based on computing-optimized algorithm
    :param n: Limit of prime numbers generator (if None then infinite loop)
    :return: Generator of prime numbers
    """
    found_primes = []
    checking_n = 2
    limit = n + 1 if n else -1
    while checking_n < limit:
        is_prime = True
        for prime in found_primes:
            if prime > int(sqrt(checking_n)) + 1:
                break
            if checking_n % prime == 0:
                is_prime = False
                break
        if is_prime:
            found_primes.append(checking_n)
            yield checking_n
        checking_n += 1


def __primes_with_memory_priority(n: Optional[int]) -> Generator[int, None, None]:
    """
    Prime numbers generator up to N based on memory-optimized algorithm
    :param n: Limit of prime numbers generator (if None then infinite loop)
    :return: Generator of prime numbers
    """
    checking_n = 2
    limit = n + 1 if n else -1
    while checking_n < limit:
        is_prime = True
        primes_loop_limit = int(sqrt(checking_n)) + 1
        for prime in range(2, primes_loop_limit):
            if checking_n % prime == 0:
                is_prime = False
                break
        if is_prime:
            yield checking_n
        checking_n += 1


def __is_positive_integer(value: Any) -> None:
    """
    Raising error if value is not positive integer
    """
    if not isinstance(value, int):
        raise TypeError(f"{type(value).__name__} is not instance of class {int.__name__}")
    if value <= 0:
        raise ValueError(f"{value} is less than or equal to 0")


if __name__ == "__main__":
    assert list(primes(1)) == []
    assert list(primes(2)) == [2]
    assert list(primes(5)) == [2, 3, 5]
    assert list(primes(10)) == [2, 3, 5, 7]
