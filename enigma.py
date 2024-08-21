import random
import string


ALPHABET = string.ascii_uppercase


class PlugBoard(object):
    def __init__(self, map_alphabet):
        self.alphabet = ALPHABET
        self.forward_map = {}
        self.backword_map = {}
        self.mapping(map_alphabet)

    def mapping(self, map_alphabet):
        self.forward_map = dict(zip(self.alphabet, map_alphabet))
        self.backward_map = {v: k for k, v in self.forward_map.items()}

    def forward(self, index_num):
        char = self.alphabet[index_num]
        char = self.forward_map[char]
        return self.alphabet.index(char)

    def backward(self, index_num):
        char = self.alphabet[index_num]
        char = self.backward_map[char]
        return self.alphabet.index(char)


class Rotor(PlugBoard):

    def __init__(self, map_alphabet, offset=0):
        super().__init__(map_alphabet)
        self.offset = offset
        self.rotations = 0

    def rotate(self, offset=None):
        if not offset:
            offset = self.offset
        self.alphabet = self.alphabet[offset:] + self.alphabet[:offset]
        self.rotations += offset
        return self.rotations

    def reset(self):
        self.rotations = 0
        self.alphabet = ALPHABET


class Refrector(object):

    def __init__(self, map_alphabet):
        self.map = dict(zip(ALPHABET, map_alphabet))
        for x, y in self.map.items():
            if x != self.map[y]:
                raise ValueError(x, y)

    def reflect(self, index_num):
        reflected_char = self.map[ALPHABET[index_num]]
        return ALPHABET.index(reflected_char)


class EnigmaMachine(object):

    def __init__(self, plug_board, rotors, reflector):
        self.plug_board = plug_board
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, text):
        return "".join([self.go_through(c) for c in list(text)])

    def decrypt(self, text):
        for rotor in self.rotors:
            rotor.reset()
        return "".join([self.go_through(c) for c in list(text)])

    def go_through(self, char):
        char = char.upper()
        if char not in ALPHABET:
            return char

        index_num = ALPHABET.index(char)
        index_num = self.plug_board.forward(index_num)

        for rotor in self.rotors:
            index_num = rotor.forward(index_num)

        index_num = self.reflector.reflect(index_num)

        for rotor in reversed(self.rotors):
            index_num = rotor.backward(index_num)

        index_num = self.plug_board.backward(index_num)
        char = ALPHABET[index_num]

        for rotor in reversed(self.rotors):
            if rotor.rotate() % len(ALPHABET) != 0:
                break

        return char


if __name__ == "__main__":
    # plug_board = PlugBoard("BADC")
    # encrypted_index = plug_board.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[plug_board.backward(encrypted_index)]
    # print(decrypted)

    # rotor = Rotor("BADC", 1)

    # encrypted_index = rotor.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)

    # rotor.rotate()

    # encrypted_index = rotor.forward(ALPHABET.index("A"))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)

    # r = Refrector("BADC")
    # i = r.reflect(ALPHABET.index("A"))
    # print(ALPHABET[i])

    get_random_alphabet = lambda: "".join(random.sample(ALPHABET, len(ALPHABET)))
    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 1)

    r = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes) / 2)):
        x = indexes.pop(random.randint(0, len(indexes) - 1))
        y = indexes.pop(random.randint(0, len(indexes) - 1))
        r[x], r[y] = r[y], r[x]
    reflector = Refrector("".join(r))

    machine = EnigmaMachine(p, [r1, r2, r3], reflector)
    s = "ATTACK SILICON VALLEY"
    e = machine.encrypt(s)
    print(e)
    d = machine.decrypt(e)
    print(d)
