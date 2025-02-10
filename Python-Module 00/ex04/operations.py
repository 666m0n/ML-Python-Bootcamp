import sys

def check_args():
	"""
	Vérifie les arguments fournis au programme
	Retourne un tuple (a, b) si les arguments sont valides
	Lève une AssertionError sinon
	"""
	if len(sys.argv) < 3:
		print("Usage : python operation.py <number1> <number2>")
		sys.exit()
	elif len(sys.argv) > 3:
		raise AssertionError("too many arguments")

	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
		return (a ,b)
	except ValueError:
		raise AssertionError("only integers")

def perform_operations(a, b):
	"""
	Effectue les opérations arithmétiques sur a et b
	et affiche les résultats
	"""
	print(f"Sum:        {a + b}")
	print(f"Difference: {a - b}")
	print(f"Product:    {a * b}")
	try:
		print(f"Quotient:   {a / b}")
	except ZeroDivisionError:
		print("Quotient:   ERROR (division by zero)")
	try:
		print(f"Remainder:  {a % b}")
	except ZeroDivisionError:
		print("Remainder:  ERROR (modulo by zero)")

if __name__ == "__main__":
	try:
		a, b = check_args()
		perform_operations(a, b)
	except AssertionError as e:
		print(f"AssertionError : {str(e)}")