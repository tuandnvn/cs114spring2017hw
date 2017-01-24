from fst import FST
import string, sys

def letters_to_numbers():
	"""
	Returns an FST that converts letters to numbers as specified by
	the soundex algorithm
	"""

	# Let's define our first FST
	f1 = FST('soundex-generate')

	# Indicate that '1' is the initial state
	f1.add_state('start')
	f1.add_state('next')
	f1.initial_state = 'start'

	# Set all the final states
	f1.set_final('next')

	return f1

def truncate_to_three_digits():
	"""
	Create an FST that will truncate a soundex string to three digits
	"""

	# Ok so now let's do the second FST, the one that will truncate
	# the number of digits to 3
	f2 = FST('soundex-truncate')

	# Indicate initial and final states
	f2.add_state('1')
	f2.initial_state = '1'
	f2.set_final('1')

	return f2

def add_zero_padding():
	# Now, the third fst - the zero-padding fst
	f3 = FST('soundex-padzero')

	f3.add_state('1')
	f3.add_state('2')
	
	f3.initial_state = '1'
	f3.set_final('2')

	return f3

def soundex_convert(name_string):
	"""Combine the three FSTs above and use it to convert a name into a Soundex"""
	pass

if __name__ == '__main__':
	user_input = raw_input().strip()
	f1 = letters_to_numbers()
	f2 = truncate_to_three_digits()
	f3 = add_zero_padding()

	if user_input:
		print("%s -> %s" % (user_input, soundex_convert(tuple(user_input))))

