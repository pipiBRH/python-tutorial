class Base:
    def __init__(self, value):
        self.value = value
        print("This is Base")


class One(Base):
    def __init__(self, value):
        super(One, self).__init__(value * 2)
        print("This is One")


class Two(Base):
    def __init__(self, value):
        super(Two, self).__init__(value + 3)
        print("This is Two")


class Ways(One, Two):
    def __init__(self, value):
        super(Ways, self).__init__(value)


foo = Ways(5)
print(Ways.mro())
