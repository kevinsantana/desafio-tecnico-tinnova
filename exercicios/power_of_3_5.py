def multiple(n: int) -> int:
    ans = []
    for x in range(1, n, 1):
        if x % 3 == 0 or x % 5 == 0:
            ans.append(x)
    return sum(ans)


if __name__ == "__main__":
    print(multiple(10))
