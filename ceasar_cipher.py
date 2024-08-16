import string
from typing import Generator, Tuple


def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue

        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]

    return result


def carsar_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = ord("Z") - ord("A") + 1
    len_alphabet = len(string.ascii_uppercase)
    for candidate_shift in range(1, len_alphabet + 1):
        reverted = ""
        for char in text:
            if char.isupper():
                alphabet = string.ascii_uppercase
            elif char.islower():
                alphabet = string.ascii_lowercase
            else:
                reverted += char
                continue

            index = alphabet.index(char) - candidate_shift
            if index < 0:
                index += len_alphabet
            reverted += alphabet[index]
        yield candidate_shift, reverted


if __name__ == "__main__":
    e = caesar_cipher("ATTACK SILICON VALLY by eginner", 3)
    print(e)
    for shift_num, decrypted in carsar_cipher_hack(e):
        print(f"{shift_num:2d}", decrypted)
