class Helpers():
	def check_prime(self, number_to_check):
		self.number_to_check = number_to_check

    	if self.number_to_check < 2:
        	return False
    	else:
        	for i in range (2, self.number_to_check):
	            if self.number_to_check % i == 0:
	                return False
	                break
	        	else:
	            	return True			
