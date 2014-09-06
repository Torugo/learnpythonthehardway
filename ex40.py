class Song(object):
	""" lyrics tring for Song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthaday to you",
					"bla bla"])

bulls_on_parade = Song(["They rally arround tha family",
						"With pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
		