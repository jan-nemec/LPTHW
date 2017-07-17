class Song(object):
    """docstring for Song"""

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    # Study Drill
    def choose_me_first_rhyme(self):
        print(self.lyrics[0])

    def choose_me_last_rhyme(self):
        print(self.lyrics[-1])

    def choosen_rhyme(self, number):
        print(self.lyrics[number])

happy_bday = Song(["Happy birthday to you.",
                   "I don't want to get sued!",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drills
skakal_pes = Song(["Skákal pes,", "přes oves,", "přes zelenou louku."])

skakal_pes.sing_me_a_song()

holka_modrooka_lyrics = ["Holka modrooka", "nesedavej u potoka.", "V potoce se voda točí,", "podemele tvoje oči."]
holka_modrooka = Song(holka_modrooka_lyrics)

holka_modrooka.sing_me_a_song()
holka_modrooka.choose_me_first_rhyme()
holka_modrooka.choose_me_last_rhyme()

print("Zadej rým, který chceš zobrazit?")
wanted_rhyme = int(input(">>> "))
holka_modrooka.choosen_rhyme(wanted_rhyme)
