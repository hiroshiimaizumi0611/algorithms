from typing import Any


class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()


def validate_format(chars: str) -> bool:
    lookup = {"{": "}", "[": "]", "(": ")"}
    stack = Stack()
    for char in chars:
        if char in lookup.keys():
            stack.push(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False

    if len(stack.stack) != 0:
        return False

    return True


if __name__ == "__main__":
    j = "{'key1': 'value1', 'key2':[1,2,3], 'key3':(1,2,3)}"
    print(validate_format(j))
