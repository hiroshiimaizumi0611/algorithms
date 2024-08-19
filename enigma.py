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


if __name__ == "__main__":
    # plug_board = PlugBoard("BADC")
    # encrypted_index = plug_board.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[plug_board.backward(encrypted_index)]
    # print(decrypted)

    rotor = Rotor("BADC", 1)

    encrypted_index = rotor.forward(ALPHABET.index('A'))
    print(ALPHABET[encrypted_index])
    decrypted = ALPHABET[rotor.backward(encrypted_index)]
    print(decrypted)

    rotor.rotate()

    encrypted_index = rotor.forward(ALPHABET.index("A"))
    print(ALPHABET[encrypted_index])
    decrypted = ALPHABET[rotor.backward(encrypted_index)]
    print(decrypted)
