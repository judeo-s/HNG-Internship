import httpx
"""
Utility functions for HNG Internship Stage 1
"""


def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False if it is not.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    """
    Checks if a number is perfect.

    A perfect number is a positive integer that is equal to the sum of its 
    proper positive divisors, excluding the number itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is perfect, False if it is not.
    """

    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(num: int) -> bool:
    """
    Checks if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits 
    each raised to the power of the number of digits.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False if it is not.
    """
    if num == 0:
        return False
    sum_of_divisors = 0
    for i in range(1, abs(num) // 2 + 1):
        if num % i == 0:
            sum_of_divisors += i
    return num == sum_of_divisors


def is_odd(num: int) -> bool:
    """
    Checks if a number is odd.

    An odd number is an integer which is not divisible by 2.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is odd, False if it is even.
    """

    return num % 2 != 0


def is_even(num: int) -> bool:
    """
    Checks if a number is even.

    An even number is an integer which is divisible by 2.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is even, False if it is odd.
    """
    return num % 2 == 0


def digit_sum(n: int) -> int:
    """
    Calculates the sum of the digits of a number.

    Args:
        n (int): The number whose digit sum is to be calculated.

    Returns:
        int: The sum of the digits of the number.
    """
    return sum(int(d) for d in str(abs(int(n))))


async def get_fun_fact(n: int) -> str:
    """
    Gets a fun fact about a number from the numbersapi.com API.

    Args:
        n (int): The number whose fun fact is to be retrieved.

    Returns:
        str: The fun fact about the number.
    """
    url = f"http://numbersapi.com/{n}/math"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
