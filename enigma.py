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
        return self.alphabet.index[char]

    def backward(self, index_num):
        char = self.alphabet[index_num]
        char = self.backward_map[char]
        return self.alphabet.index[char]


if __name__ == "__main__":
    plug_board = PlugBoard("BADC")
    encrypted_index = plug_board.forward(ALPHABET.index('A'))
    print(ALPHABET[encrypted_index])
    decrypted = ALPHABET[plug_board.backward(encrypted_index)]
    print(decrypted)
