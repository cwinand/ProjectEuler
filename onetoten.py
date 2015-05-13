from functools import reduce
import operator

class Four():
	#future optimization: don't loop through 999 to 100 at once, break it into 100 count chunks since likely answer is between 999 and 900 
	def is_palindrome(self, num):
		self.num = str(num)
		self.reversed_num = self.num[::-1]

		if self.num == self.reversed_num:
			return True
		else:
			return False

	def get_all_palindromes(self):
		self.three_digit_numbers = range(999, 100, -1)
		self.all_palindromes = []

		for i in self.three_digit_numbers:
			for j in self.three_digit_numbers:
				if self.is_palindrome(i * j):
					self.all_palindromes.append(i * j)

		return self.all_palindromes

	def answer(self):
		self.all_palindromes = self.get_all_palindromes()
		return max(self.all_palindromes)


class Eight():
	def __init__(self):
		self.series = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	
	def get_number_blocks(self):
		self.number_blocks = []

		#this range goes through every consecutive 'block' of thirteen characters
		for i in range(0, len(self.series) - 13):
			self.thirteen_count_block = self.series[i:i+13]
			#zeros in the block will always lead to a product = 0
			if '0' in self.thirteen_count_block:
				continue

			self.number_blocks.append(([int(i) for i in self.thirteen_count_block]))

		return self.number_blocks
		
	def get_number_block_products(self):
		self.number_blocks = self.get_number_blocks()
		self.number_block_products = []

		for i in self.number_blocks:
			self.number_block_products.append(reduce(operator.mul, i))

		return self.number_block_products

	def answer(self):
		self.number_block_products = self.get_number_block_products()
		return max(self.number_block_products)
