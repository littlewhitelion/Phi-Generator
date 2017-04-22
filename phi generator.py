#This program is to prompt the user to ask how many decimals places they want the number phi displayed to

import math
from decimal import *

def phi():
	user1 = input("Desired phi length: ")
	getcontext().prec = user1
	phi1 = (1 + Decimal(5).sqrt())/2
	print phi1

phi()