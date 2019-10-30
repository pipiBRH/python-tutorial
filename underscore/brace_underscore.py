class Pe:

    __qualname__ = 'ehuang02'

    def __init__(self, domain):
        self.domain = domain

    def get_fqdn(self):
        """Get fully qulified name."""
        return self.__qualname__ + '.' + self.domain


print(Pe("yahoo.com").get_fqdn())