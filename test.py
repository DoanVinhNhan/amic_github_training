def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n (n!).

    Raises:
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
        
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)
