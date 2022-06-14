def factorial(n: int) -> int:
    if n < 2:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(2))
