class Base:
    def __init__(self, value):
        self.value = value
        print("This is Base")


class One(Base):
    def __init__(self, value):
        super(One, self).__init__(value)
        self.value *= 2
        print("This is One")


class Two(Base):
    def __init__(self, value):
        super(Two, self).__init__(value)
        self.value += 3
        print("This is Two")


class Ways(One, Two):
    def __new__(cls, value):
        instance = object.__new__(cls)
        return instance

    def __init__(self, value):
        super(Ways, self).__init__(value)


# class Ways2(Two,Ways):
#     def __init__(self, value):
#         super(Ways, self).__init__(value)


foo = Ways(5)
print(foo.value)

# print(Ways)
