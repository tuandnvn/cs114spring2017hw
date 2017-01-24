import fst

class Parser():

	def __init__(self):
		pass

	def generate(self, analysis):
		"""Generate the morphologically correct word 

		e.g.
		p = Parser()
		analysis = ['p','a','n','i','c','+past form']
		p.generate(analysis) 
		---> 'panicked'
		"""
		output = ['p','a','n','i','c','k','e','d']
		return ''.join(output)

	def parse(self, word):
		"""Parse a word morphologically 

		e.g.
		p = Parser()
		word = ['p', 'a', 'n', 'i', 'c', 'k','e','d']
		p.parse(word)
		---> 'panic+past form'
		"""
		output = ['p','a','n','i','c','+past form']
		return ''.join(output)

