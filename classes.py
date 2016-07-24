


class Foo:
	pass

class Pokemon:
	'this class has information about pokemons'

	def __init__(self, pokemon_name,pokemon_cp,pokemon_type):
		self.pokemon_name = pokemon_name
		self.pokemon_cp = pokemon_cp
		self.pokemon_type = pokemon_type
		self.__foo = 'private variable'

	def displayInfo(self):
		print self.__foo
		print "My Pokemon is %s, with cp %s, and type is %s"%(self.pokemon_name,
			self.pokemon_cp,
			self.pokemon_type)
		print self.foo()

	def foo(self):
		return 42



if __name__ == '__main__':
	pikachu = Pokemon('Pikachu','100','electricity')
	print pikachu.pokemon_name
	#print pikachu.__foo
	pikachu.displayInfo()
	print dir(pikachu)
	print type(pikachu)
	print type(Pokemon)
	print dir(Pokemon)
	print pikachu.__doc__




