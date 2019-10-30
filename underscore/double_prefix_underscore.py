class Ethan:

    title = 'Production engineer'
    location = 'LinKo'
    favorite_movie = 'terminator'
    hobby = 'coding'
    __mentor = 'bfan'

    def profile(self):
        """Print my personal profile."""
        print(f'''
            I live in {self.location}
            My favorite movie is {self.favorite_movie}
            My hobby is {self.hobby}
            My mentor is {self.__mentor}
        ''')


class Cola(Ethan):

    location = 'DaAn'
    favorite_movie = 'Brokeback Mountain'
    hobby = 'compose bl story'
    __mentor = 'yhsueh'


Ethan().profile()

c = Cola()
c.profile()
# print(c.__mentor)
# print(c._Cola__mentor)

