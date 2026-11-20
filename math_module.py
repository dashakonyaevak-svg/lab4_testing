def factorial(n):
    """Повертає факторіал невід'ємного цілого числа."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал від'ємного числа не визначений")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n):
    """Перевіряє, чи є число парним."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    return n % 2 == 0