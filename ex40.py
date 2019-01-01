class song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_paradise = song(["They rally around the family",
                        "With pockets full of shell"])

happy_bday.sing_me_a_song()

bulls_on_paradise.sing_me_a_song()
