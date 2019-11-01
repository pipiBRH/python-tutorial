class Base:
    def __init__(self, value):
        self.value = value
        print(f"This is Base")


class One(Base):
    def __init__(self, value):
        Base.__init__(self, value)
        self.value *= 2
        print(f"This is One")


class Two(Base):
    def __init__(self, value):
        Base.__init__(self, value)
        self.value += 3
        print(f"This is Two")


class Ways(One, Two):
    def __init__(self, value):
        One.__init__(self, value)
        Two.__init__(self, value)


foo = Ways(5)
print(foo.value)
