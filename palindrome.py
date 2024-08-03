# s = "racecar"
# print(s == "".join(reversed(s)))

# print(s == s[::-1])


def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True

    start, end = 0, len_strings - 1
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))
