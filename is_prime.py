def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    print(is_prime_v1(10))
