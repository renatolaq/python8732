class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
    pass


if __name__ == '__main__':
    b = Borg()
    b1 = Borg()
    b.x = 4

    print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
    print("Borg Object 'b1': ", b1)
    print("Object State 'b':", b.__dict__)  ## b and b1 share same state
    print("Object State 'b1':", b1.__dict__)
    