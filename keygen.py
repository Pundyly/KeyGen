import random
import string

#setup
version = "0.1"
print("Welcome in KeyGen " + version)
print("Print amount of passwords: ")
amounts = input()
num_amounts = int(amounts)
print("Print amount of symbols: ")
amountsofsymbols = input()
num_amountsofsymbols = int(amountsofsymbols)
print("Symbols to be used( all to all symbols): ")
symbols = input()
if symbols == "all":
	symbols = string.ascii_letters + string.digits + string.punctuation

#log

print("##################")
print("Amount of passwords: " + amounts)
print("Amount of symbols: " + amountsofsymbols)
print("Symbols: " + symbols)
print("##################")

#keygen
while num_amounts > 0:
	password = ""
	num_temp_amountsofsymbols = num_amountsofsymbols
	while num_temp_amountsofsymbols > 0:
		password += random.choice(symbols)
		num_temp_amountsofsymbols = num_temp_amountsofsymbols - 1
		pass
	print(password)
	num_amounts = num_amounts - 1
	pass