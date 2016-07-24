
#from bar import count
import bar
import math

def hello():
	#print 'Hello World'
	#print 1001233*3
	#print 'pokemon %s'%('go')
	print 'asdasd'

def vowelcount(a):
	count = 0
	for char in a:
		if char.lower() in 'aeiou':
			count = count +1
	return count

def vowelcount2(a):
	count = 0
	for char in a:
		if char in 'aeiouAEIOU':
			count = count +1
	return count

def main():
	a = input()
	print math.sqrt( a )
	#print vowelcount( int(a) )

def favorite_pokemon(cp,pokemon_type='water'):
	print type(cp)
	print cp
	if pokemon_type == 'fire':
		return 'pikachu' 
	elif pokemon_type == 'water':
		return 'squirtle'
	elif pokemon_type == 'grass':
		return 'bulbasaur'

def list_pokemons(*str):
	print type(str)
	for i in str:
		print i

def list_pokemons2(**elephant):
	print type(elephant)
	print elephant.keys()

	for key,value in elephant.items():
		print key,value


if __name__ == '__main__':
	#foo(1,2,3,4,5)
	list_pokemons('bulbasaur','pikachu','squirtle','zz')
	'''
	list_pokemons2(a='pikachu',
		b='bulbasaur',
		c='squirtle',
		d='zz',
		e='snorlax')
	'''
	#a = input()
	#b = raw_input()
	#print favorite_pokemon(cp,pokemon_type)


